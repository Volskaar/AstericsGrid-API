echo Tests with known subjects / known verbs
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "ICH HABEN VIEL GELD"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "DU ESSEN GERNE PIZZA"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "OPA SEIN SEHR ALT"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "WIR TRINKEN GERNE COLA"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "IHR SEHEN EINEN LOEWEN"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "FREUNDE SPIELEN GERNE CLUEDO"
echo .

echo Tests without known verb (should fail)
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "ICH WOLLEN SUSHI"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "DU SOLLEN NICHT RAUCHEN"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "OPA SCHREIEN DIE VÖGEL AN"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "WIR KIPPEN UM"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "IHR BRAUCHEN MEHR SCHLAF"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "FREUNDE KOENNEN NICHT LAUFEN"
echo .

echo Tests without known subject (should default to 3. case)
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "LOEWE HABEN KEINE ZAEHNE"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "SIE TRINKEN GERNE EISTEE"
curl -X POST http://127.0.0.1:5000/spacy -H "Content-Type: text/plain" -H "charset=utf-8" -d "LEUTE FEIERN FESTE"
echo .