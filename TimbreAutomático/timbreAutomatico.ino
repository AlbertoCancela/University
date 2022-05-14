#include "Separador.h" //Clase para separar cadenas de texto
Separador S; //instancia del separador
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include "RTClib.h"
LiquidCrystal_I2C lcd(0x27, 16, 2);
RTC_DS1307 RTC;
int hora, minuto, segundo;
void setup()
{
  Wire.begin(); // Inicia el puerto I2C
  
  RTC.begin(); // Inicia la comunicaci¢n con el RTC
//RTC.adjust(DateTime(_DATE, __TIME_));  // Establece la fecha y hora (Comentar una vez establecida la hora)
//el anterior se usa solo en la configuracion inicial
pinMode(13, OUTPUT);
digitalWrite(13,HIGH);
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.clear();
}

String cadena;
String elemento[17];
String elemento2[18];
int contador = 0;
void loop() //Función principal Loop
{  

DateTime now = RTC.now(); // Obtiene la fecha y hora del RTC
   

lcd.setCursor(0,0);
lcd.print("D:");
lcd.print(now.year(), DEC);
lcd.print("/");
lcd.print(now.month(), DEC);
lcd.print("/");
lcd.print(now.day(), DEC);
lcd.print(" ");
lcd.setCursor(0,1);
lcd.print("T: ");
lcd.print(now.hour()+1, DEC);
lcd.print(":");
lcd.print(now.minute(), DEC);
lcd.print(":");
lcd.print(now.second(), DEC);
hora=now.hour()+1;
minuto=now.minute();
segundo=now.second();


 if (Serial.available()>0){
  if (contador==0){
    cadena = Serial.readString();
    
 for (int i = 0; i <=17; i++)
  {
    elemento[i - 1] = S.separa(cadena, ':', i - 1);
  }
  Serial.println("Trama1: "+elemento[0]+elemento[1]+
                            elemento[2]+elemento[3]+
                            elemento[4]+elemento[5]+
                            elemento[6]+elemento[7]+
                            elemento[8]+elemento[9]+
                            elemento[10]+elemento[11]+
                            elemento[12]+elemento[13]+
                            elemento[14]+elemento[15]);
    }
   if (contador==1){
    cadena = Serial.readString();
    
 for (int i = 0; i <=18; i++)
  {
    elemento2[i - 1] = S.separa(cadena, ':', i - 1);
  }
   Serial.println("Trama2: "+elemento2[0]+elemento2[1]+
                            elemento2[2]+elemento2[3]+
                            elemento2[4]+elemento2[5]+
                            elemento2[6]+elemento2[7]+
                            elemento2[8]+elemento2[9]+
                            elemento2[10]+elemento2[11]+
                            elemento2[12]+elemento2[13]+
                            elemento2[14]+elemento2[15]+elemento2[16]);
    
    }
    if (contador==2){
    cadena = Serial.readString();
    
    Serial.println("Trama3: "+elemento[0]+elemento[1]+elemento2[0]);
    }
    contador++;
}

  if (contador == 2)
  {
   if (elemento2[16].toInt() >= 0 && elemento2[16].toInt() <=4)
        {
         for (int i = 0; i <=15; i++)
        {
          if(elemento[i].toInt() == hora && elemento[i+1].toInt() == minuto && segundo >= 0 && segundo <=3)
          {
            lcd.print("ok");
            digitalWrite(13,LOW);
            delay(3000);
            digitalWrite(13, HIGH);
          }
          i++;
        }
        }
        else if (elemento2[16].toInt() == 5)
        {
        for (int i = 0; i <=15; i++)
        {
          if(elemento2[i].toInt() == hora && elemento2[i+1].toInt() == minuto && segundo >= 0 && segundo <= 3)
          {
            lcd.print("ok");
            digitalWrite(13,LOW);
            delay(3000);
            digitalWrite(13, HIGH);
          }
          i++;
        }  
        }
  }
         
delay(1000); // La información se actualiza cada seg.
lcd.setCursor(0,0);
lcd.print("                  ");
lcd.setCursor(0,1);
lcd.print("                  ");
  }
