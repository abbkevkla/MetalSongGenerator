# MetalSongGenerator

## Vad har jag gjort?
Syftet med detta projekt var att kunna generera nya metal-låtar med hjälp av AI, genom att träna en model på olika metallåtar och sedan generera musik utifrån den modellen. Dessutom ville jag genera en text att ha till musiken, och om möjligt spela upp båda samtidigt.

För att skapa musiken använda jag [MusicAutoBot](https://github.com/bearpelican/musicautobot), skrivet av Andrew Shaw. MusicAutoBot använder FastAi's deep learning bibliotek och Music21. All kod i mappen "musicautobot-master" är tagen från Andrew Shaws projekt och är omskrivet för att passa mina behov. Ifall man vill testa koden finns det Notebooks i [mappen av samma namn](Notebooks). Programmet kräver programmet MuseScore 3 för att man ska kunna visualisera musiken, men man kan fortfarande träna och generera musiken och jag tror det går att spela upp resultaten i Notebooken. Jag är dock osäker på om det går att spara resultatet utan MuseScore.

För att skriva texter till musiken har jag använt NLP (Natural Language Processing), i det här fallet en GPT2-variant, som ni hittar [här](https://colab.research.google.com/drive/1OG1HxBMdIMyWfc0qP2rz6tvQwtx9Gikn), skriven av Max Woolf. Jag har inte laddat upp den i Github, dels för att koden inte behövdes skrivas om och för att jag använde Google Collabs för att köra den. Jag använder även ett pythonscript för att läsa upp texterna jag skriver till .wav filer. Sedan gör jag om de till .mp3 filer och kombinerar texten med musiken för att få en "låt".

## Instruktion
Projektet består av 5 delar. Träna en modell, generera musik med modellen, generera en text, läsa upp texten och slutligen sätta ihop text och musik. Alla notebooks ska bara vara att köra utan några större ändringar. Det som behöver ändras är alla paths, men utöver det ska det inte vara några större problem.

För att träna en modell använder man [Train_music](Notebooks/Train_music.ipynb). Denna rekommenderar jag att använda i Google Colab så att det går fortfare.
Om du inte vill träna en egen modell finns det massvis med modeller som jag redan tränat i mappen [models](musicautobot-master/data/numpy/models). Tydligen är modellerna för stora för github, så om du verkligen behöver någon modell kan du antingen kolla på Andrew Shaw's version, där det finns modeller, eller fråga mig om det.

Generering av musik görs med [Generate_Music](Notebooks/Generate_music.ipynb). Denna är gjord för att köras lokalt på din dator, med exempelvis Jupyter, men den går säkert att skriva om ifall man föredrar att köra Google Colab. 

Generering av text hittar du ovan där jag förklarar vad jag använt.

För att läsa upp texten finns det ett [pythonscript](Results/Lyrics/textreader.py) i Results mappen. Denna genererar .wav filer. Här används tredjepartsbiblioteket comtypes.

Slutligen, för att sätta ihop ljud och text finns det [Music_Lyrics_Combiner](Notebooks/Music_Lyrics_Combiner.ipynb) notebooken. Denna kör du i Google Colab.

## Varför denna metod?
Den simpla anledningen till att jag valde MusicAutoBot för att generera musik var för att man använder midi-filer vid träning av modeller. Midi filer innehåller musikdata och är väldigt lätta attt hitta, men även lätta att modifiera vid behov, vilket skulle låta mig kontrollera precis vad programmet ska lära sig. Jag vet att det finns andra metoder för att genera musik, men jag ville göra mitt projekt så personligt som möjligt, så därför blev det musicautobot.

## Resultatet
I mappen [Results](Results) kan du se resultaten från projektet. 

## Reflektion
Som man ser i resultatet så skulle jag inte kalla projektet lyckat. Jag lyckades inte få musicautobot att fungera ordentligt, och därför kunde jag inte generera någon vetig musik. Det är trist att det gick som det som gick, men jag har iallafall kunnat ta några lärdomar från mitt misslyckande.
* Jag har lärt mig att man alltid ska kolla så att saker funkar innan man kör. Jag började i fel ända med det här projektet. Jag försökte först att träna min egen model, vilket tog alldeles för mycket tid. Dels för att jag var tvungen att göra om lite i koden för att det skulle funka att träna, men också för att jag var tvungen att hantera all data. Vad jag borde ha gjort var att först testa med den förtränade modellen och kollat så att den fungerade. Nu upptäckte jag alldeles för sent att det inte gick att generera musik ordentligt, och då var det för sent att ändra sig. Hade jag testat för sånt här som det första jag gjorde hade jag kunnat byta tillvägagångssätt i början av projektet och inte slösa en massa tid. 
* Något som går ihop med det jag skrev ovan är vikten av planering. Jag borde ha planerat vad jag behövde göra, sedan göra research på vad det fanns för metoder. På så vis hade arbetsprocessen inte blivit så hackig när man måste avbryta arbetet för att sitta och googla fram en lösning. Dessutom hade man tidigare kunnat ta reda på vad som funkar och inte, och utforma projektet utefter det.
* Jag har fördjupat min Python och AI kunskap. Eftersom att musicautobot strulade en hel del har jag fått göra väldigt mycket felsökning och försökt att förstå mig på vad som verkligen händer i scripten. Dessutom var musicautobot skrivet för en annan sorts notebook variant än vad jag använt (jag använde Jupyter), vilket krävde lite jobb för att ställa om ordentligt. Så trots att jag inte skrivit så mycket av koden känner jag mig mer bekväm med de metoder jag använt.
* Har lärt mig lite om filhantering, dels hur man gör om och redigerar midi-filer, men även hur man refererar till olika filer på olika vis och även hur man ställer om en environment path.
* Jag har lärt mig läsa noter till viss mån på grund av alla midi-filer jag har redigerat. Kanske inte så användbart i programmeringsyfte, men kul ändå. 

## Som alltid avslutas min Readme med en bil
Den här gången blev det en Subaru

![](Subaru_WRX.jpg)

