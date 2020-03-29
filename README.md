# MetalSongGenerator

## Vad har jag gjort?
Syftet med detta projekt var att kunna generera nya metal-låtar med hjälp av en AI, genom att träna en model på olika metallåtar och sedan generera musik utifrån den modellen. Dessutom ville jag genera en text att ha till musiken, och om möjligt spela upp båda samtidigt.

För att skapa musiken använda jag [MusicAutoBot](https://github.com/bearpelican/musicautobot), skrivet av Andrew Shaw. MusicAutoBot använder FastAi's deep learning bibliotek och Music21. All kod i mappen "musicautobot" är tagen från Andrew Shaws projekt och är omskrivet för att passa mina behov. Ifall man vill testa koden finns det Notebooks i mappen av samma namn. Programmet kräver programmet MuseScore 3 för att man ska kunna visualisera musiken, men man kan fortfarande träna och generera musiken och jag tror det går att spela upp reslutaten i Notebooken.

För att skriva texter till musiken har jag använt NLP (Natural Language Processing), i det här fallet en GPT-variant, som ni hittar [här](https://colab.research.google.com/drive/1OG1HxBMdIMyWfc0qP2rz6tvQwtx9Gikn), skriven av Max Woolf. Jag har inte laddat upp den i Githuben, dels för att koden inte behövdes skrivas om och för att jag använde Google Collabs för att köra den. Jag la även till python-scriptet textreader.py för att läsa upp texten till en .mp3 fil. Till detta användes tredjepartsbiblioteket comtypes.

## Varför denna metod?
Den simpla anledningen till att jag valde MusicAutoBot är för att man använder midi-filer vid träning av modeller. Midi filer innehåller all musik och är väldigt lätta hitta, men även lätta att modifiera vid behov, vilket skulle låta mig kontrollera precis vad programmet ska lära sig. Jag vet att det finns andra metoder för att genera musik, men jag ville göra mitt projekt så personligt som möjligt, så därför blev det musicautobot.

## Resultatet
I mappen results kan du se resultaten från projektet. 

## Reflektion

## Lärdomar
