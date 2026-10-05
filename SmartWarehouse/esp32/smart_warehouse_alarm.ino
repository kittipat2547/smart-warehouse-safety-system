#include <WiFi.h>
#include <WebServer.h>

const char* WIFI_SSID = "YOUR_WIFI_NAME";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

const int BUZZER_PIN = 25;
const int WARNING_LED_PIN = 26;

WebServer server(80);

void alarmOn() {
  digitalWrite(BUZZER_PIN, HIGH);
  digitalWrite(WARNING_LED_PIN, HIGH);
}

void alarmOff() {
  digitalWrite(BUZZER_PIN, LOW);
  digitalWrite(WARNING_LED_PIN, LOW);
}

void handleAlarm() {
  alarmOn();
  server.send(200, "text/plain", "ALARM ON");

  delay(2000);

  alarmOff();
}

void handleStatus() {
  server.send(200, "text/plain", "ESP32 Smart Warehouse OK");
}

void setup() {
  Serial.begin(115200);

  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(WARNING_LED_PIN, OUTPUT);

  alarmOff();

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  Serial.print("Connecting WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected");
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());

  server.on("/alarm", HTTP_GET, handleAlarm);
  server.on("/status", HTTP_GET, handleStatus);

  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}
