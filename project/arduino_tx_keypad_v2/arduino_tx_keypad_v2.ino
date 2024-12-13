// arduino-tx-keypad-v2
//
// Sketch for transmitting data using "ggwave"
//

#include <ggwave.h>
#include <Keypad.h>

// Pin configuration
// const int kPinButton1 = 4;
const int kPinLed0    = A14; // D13 
const int kPinSpeaker = A16; // D14
const int kPinButton0 = A6; // D12
const int kPinButton1 = A7;// D11
const int samplesPerFrame = 128;
const int sampleRate      = 6000;

// Global GGwave instance
GGWave ggwave;

char txt[64];
#define P(str) (strcpy_P(txt, PSTR(str)), txt)

// keypad
const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {5, 18, 19, 21}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {27, 26, 25, 33}; //connect to the column pinouts of the keypad
//Create an object of keypad
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

String inputString = ""; // String to hold the input

// Define the mapping of codes to messages
const char* codes[] = {
  "1", "2", "3", "4", "5", "6", "7", "8", "9",
  "101", "102", "103", "104", "105", "106", "107", "108",
  "201", "202", "203", "204", "205", "206", "207", "208",
  "301", "302", "303", "304", "305", "306", "307", "308",
  "401", "402", "403", "404", "405", "406", "407", "408",
  "911", "999",
  "500"
};

const char* messages[] = {
  "Yes", "No", "Help!", "OK", "Stop", "Go", "Up", "Down", "Wait",
  "All clear", "Low air", "Low battery", "Need rest", "Need assist", "Found item", "Lost item", "Surface now",
  "Move left", "Move right", "Move forward", "Move back", "Ascend slow", "Descend slow", "Hold position", "Follow me",
  "Clear water", "Murky water", "Strong current", "Calm water", "Cold water", "Warm water", "High visibility", "Low visibility",
  "Shark nearby", "Jellyfish swarm", "Strong current", "Entangled", "Equip failure", "Diver injury", "Decomp issue", "Lost buddy",
  "Help!", "Help!",
  "Unstoppable Tech"
};


// Helper function to output the generated GGWave waveform via a buzzer
void send_text(GGWave & ggwave, uint8_t pin, const char * text, GGWave::TxProtocolId protocolId) {
    Serial.print(F("Sending text: "));
    Serial.println(text);

    ggwave.init(text, protocolId);
    ggwave.encode();

    const auto & protocol = GGWave::Protocols::tx()[protocolId];
    const auto tones = ggwave.txTones();
    const auto duration_ms = protocol.txDuration_ms(ggwave.samplesPerFrame(), ggwave.sampleRateOut());
    for (auto & curTone : tones) {
        const auto freq_hz = (protocol.freqStart + curTone)*ggwave.hzPerSample();
        tone(pin, freq_hz);
        delay(duration_ms);
    }

    noTone(pin);
    digitalWrite(pin, LOW);
}

void send_via_audio(const char * text) {
  send_text(ggwave, kPinSpeaker, text, GGWAVE_PROTOCOL_MT_FASTEST);
  delay(250);
}

void send_key(char key) {
    char myArray[2]; // 2 elements to include the null terminator

    myArray[0] = key;
    myArray[1] = '\0'; // Null-terminate the array
    send_via_audio(P(myArray));

}

void send_team_name() {
  send_via_audio(P("Unstoppable Tech"));
}
void send_team_members() {
    send_via_audio(P("Aanya"));
    delay(500);
    send_via_audio(P("Anaya"));
    delay(500);
    send_via_audio(P("Avanti"));
    delay(500);
    send_via_audio(P("Nivedh"));
    delay(500);
    send_via_audio(P("Rupa"));
    delay(500);
    send_via_audio(P("Sahithi"));
    delay(500);
    send_via_audio(P("Sanvi"));
    delay(500);
    send_via_audio(P("Surbhi"));
}

void setup() {
    Serial.begin(115200);
    while (!Serial);

    pinMode(kPinLed0,    OUTPUT);
    pinMode(kPinSpeaker, OUTPUT);
    // pinMode(kPinButton0, INPUT);
    // pinMode(kPinButton1, INPUT);

    // Initialize "ggwave"
    {
        Serial.println(F("Trying to initialize the ggwave instance"));

        ggwave.setLogFile(nullptr);

        auto p = GGWave::getDefaultParameters();

        // Adjust the "ggwave" parameters to your needs.
        // Make sure that the "payloadLength" parameter matches the one used on the transmitting side.
        p.payloadLength   = 16;
        p.sampleRateInp   = sampleRate;
        p.sampleRateOut   = sampleRate;
        p.sampleRate      = sampleRate;
        p.samplesPerFrame = samplesPerFrame;
        p.sampleFormatInp = GGWAVE_SAMPLE_FORMAT_I16;
        p.sampleFormatOut = GGWAVE_SAMPLE_FORMAT_U8;
        p.operatingMode   = GGWAVE_OPERATING_MODE_TX | GGWAVE_OPERATING_MODE_TX_ONLY_TONES | GGWAVE_OPERATING_MODE_USE_DSS;

        // Protocols to use for TX
        GGWave::Protocols::tx().only(GGWAVE_PROTOCOL_MT_FASTEST);

        // Sometimes, the speaker might not be able to produce frequencies in the Mono-tone range of 1-2 kHz.
        // In such cases, you can shift the base frequency up by changing the "freqStart" parameter of the protocol.
        // Make sure that in the receiver (for example, the "Waver" app) the base frequency is shifted by the same amount.
        // Here we shift the frequency by +48 bins. Each bin is equal to 48000/1024 = 46.875 Hz.
        // So the base frequency is shifted by +2250 Hz.
        //GGWave::Protocols::tx()[GGWAVE_PROTOCOL_MT_FASTEST].freqStart += 48;

        // Initialize the ggwave instance and print the memory usage
        ggwave.prepare(p);
        Serial.println(ggwave.heapSize());

        Serial.println(F("Instance initialized successfully!"));
    }
}

void loop() {


  char key = keypad.getKey(); // Get the key pressed

  if (key) { // If a key is pressed
    Serial.print("Key Pressed : ");
    Serial.println(key);
    if (key == '#') { // If the key is the hash key
      bool found = false;
      for (int i = 0; i < sizeof(codes) / sizeof(codes[0]); i++) {
        if (inputString == codes[i]) {
          Serial.println("Message: " + String(messages[i])); // Print the corresponding message
          found = true;
          send_via_audio(messages[i]);
          break;
        }
      }
      if (inputString == "501") {
        send_team_members();
        found = true;
      }
      if (!found) {
        Serial.println("Unknown code"); // Print an error message if the code is not found
      }
      inputString = ""; // Clear the input string
    } else {
      inputString += key; // Append the key to the input string
    }
  }    
}
