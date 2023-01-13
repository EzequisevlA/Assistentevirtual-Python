const SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition
const SpeechGrammarList = window.SpeechGrammarList || webkitSpeechGrammarList
const SpeechRecognitionEvent = window.SpeechRecognitionEvent || webkitSpeechRecognitionEvent
const recognition = new SpeechRecognition()
recognition.interimResults = true
const synth = window.speechSynthesis
const speak = (text) =>{
    const uterance = new SpeechSynthesisUtterance(text)
    synth.speak(uterance)}



function ouvir(){
    
    let resposta = document.createElement('p')
    let txtos = document.getElementById('texts')
    recognition.start()
    isRecording = false
    
    recognition.addEventListener('result', (e) =>{
        console.log(e.results)
    
        var texto = Array.from(e.results)
            .map(result => result[0].transcript)
            .join('')
    
        resposta.innerText = texto
        txtos.appendChild(resposta)
        if(texto.includes('iniciar gravação')){
            isRecording = true
        }
    
    
        
        if(texto.includes('olá') || texto.includes('Olá') ||texto.includes('ola') ||texto.includes('lola')||texto.includes(' Olá')||texto.includes(' olá')){
            speak("Olá, eu sou a sua assistente virtual, como posso ajudar?")
            isRecording = false
            
        }
    })
    
}
ouvir()


