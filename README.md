# MetalSongGenerator

## Vad har jag gjort?
Syftet med detta projekt var att kunna generera nya metal-låtar med hjälp av en AI, genom att träna en model på olika metallåtar och sedan generera låtar utifrån den modellen. För att göra detta använda jag [MusicAutoBot](https://github.com/bearpelican/musicautobot), skrivet av Andrew Shaw. MusicAutoBot använder FastAi's deep learning bibliotek och Music21. All kod i mappen "musicautobot" är tagen från Andrew Shaws projekt och är omskrivet för att passa mina behov.

För att skriva texter till musiken har jag använt NLP (Natural Language Processing), i det här fallet en GPT-variant, som ni hittar [här](https://colab.research.google.com/drive/1OG1HxBMdIMyWfc0qP2rz6tvQwtx9Gikn), skriven av Max Woolf. Jag har inte laddat upp den i Githuben, dels för att koden inte behövdes skrivas om och för att jag använde Google Collabs för att köra den.

## Varför denna metod?
Den simpla anledningen till att jag valde just MusicAutoBot är för att man använder midi-filer vid träning av modeller. Midi filer innehåller all musik och är väldigt lätta hitta, men även lätta att modifiera vid behov, vilket skulle låta mig kontrollera precis vad programmet ska lära sig. 

## Resultatet
I mappen results kan du se resultaten från projektet. 

## Reflektion

## Lärdomar
