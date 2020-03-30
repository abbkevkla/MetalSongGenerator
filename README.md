# MetalSongGenerator

## Vad har jag gjort?
Syftet med detta projekt var att kunna generera nya metal-låtar med hjälp av AI, genom att träna en model på olika metallåtar och sedan generera musik utifrån den modellen. Dessutom ville jag genera en text att ha till musiken, och om möjligt spela upp båda samtidigt.

För att skapa musiken använda jag [MusicAutoBot](https://github.com/bearpelican/musicautobot), skrivet av Andrew Shaw. MusicAutoBot använder FastAi's deep learning bibliotek och Music21. All kod i mappen "musicautobot-master" är tagen från Andrew Shaws projekt och är omskrivet för att passa mina behov. Ifall man vill testa koden finns det Notebooks i [mappen av samma namn](Notebooks). Programmet kräver programmet MuseScore 3 för att man ska kunna visualisera musiken, men man kan fortfarande träna och generera musiken och jag tror det går att spela upp resultaten i Notebooken.

För att skriva texter till musiken har jag använt NLP (Natural Language Processing), i det här fallet en GPT-variant, som ni hittar [här](https://colab.research.google.com/drive/1OG1HxBMdIMyWfc0qP2rz6tvQwtx9Gikn), skriven av Max Woolf. Jag har inte laddat upp den i Github, dels för att koden inte behövdes skrivas om och för att jag använde Google Collabs för att köra den. Jag la även till ett [pythonscript](textreader.py) för att läsa upp texten till en .mp3 fil. Till detta användes tredjepartsbiblioteket comtypes.

## Varför denna metod?
Den simpla anledningen till att jag valde MusicAutoBot för att generera musik var för att man använder midi-filer vid träning av modeller. Midi filer innehåller musikdata och är väldigt lätta attt hitta, men även lätta att modifiera vid behov, vilket skulle låta mig kontrollera precis vad programmet ska lära sig. Jag vet att det finns andra metoder för att genera musik, men jag ville göra mitt projekt så personligt som möjligt, så därför blev det musicautobot.

## Resultatet
I mappen Eesults kan du se resultaten från projektet. 

## Reflektion
Som man ser i resultatet så skulle jag inte kalla projektet lyckat. Jag lyckades inte få musicautobot att fungera ordentligt, och därför kunde jag inte generera någon vetig musik. Det är trist att det gick som det som gick, men jag har iallafall kunnat ta några lärdomar från mitt misslyckande.
* Jag har lärt mig att man alltid ska kolla så att saker funkar innan man kör. Jag började i fel ända med det här projektet. Jag försökte först att träna min egen model, vilket tog alldeles för mycket tid. Dels för att jag var tvungen att göra om lite i koden för att det skulle funka att träna, men också för att jag var tvungen att hantera all data. Vad jag borde ha gjort var att först testa med den förtränade modellen och kollat så att den fungerade. Nu upptäckte jag alldeles för sent att det inte gick att generera musik ordentligt, och då var det för sent att ändra sig. Hade jag testat för sånt här som det första jag gjorde hade jag kunnat byta tillvägagångssätt i början av projektet och inte slösa en massa tid. 
* Jag har fördjupat min Python och AI kunskap. Eftersom att musicautobot strulade en hel del har jag fått göra väldigt mycket felsökning och försökt att förstå mig på vad som verkligen händer i scripten. Dessutom var musicautobot skrivet för en annan sorts notebook variant än vad jag använt (jag använde Jupyter), vilket krävde lite jobb för att ställa om ordentligt. Så trots att jag inte skrivit så mycket av koden känner jag mig mer bekväm med de metoder jag använt.
* Har lärt mig lite om filhantering, dels hur man gör om och redigerar midi-filer, men även hur man refererar till olika filer på olika vis och även hur man ställer om en environment path.
* Jag har lärt mig läsa noter till viss mån på grund av alla midi-filer jag har redigerat. Kanske inte så användbart i programmeringsyfte, men kul ändå. 

## Som alltid avslutas min Readme med en bil
Den här gången blev det en Subaru

![](Subaru_WRX.jpg)

