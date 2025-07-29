import './App.css'
import {Spotlight} from './components/ui/spotlight-new'
import {FlipWords} from './components/ui/flip-words'
import {HoverBorderGradient} from './components/ui/hover-border-gradient'

function App() {
  const words = ["faster.", "easier.", "stress free.", "with AI."];
  const title = "ClassVoyant";
  const subtitle = "Pick your classes, get your schedule";
  const buttonText = "Find your classes";
  const buttonLink = "http://localhost:8000/api/courses/";

  return (
    <main className="relative min-h-screen w-full bg-black/[0.96] antialiased bg-grid-white/[0.02] overflow-hidden flex items-center justify-center">
      <Spotlight></Spotlight>
        <div className="relative z-10">
          <h1 className="text-4xl text-white text-center">{title}</h1>
          <h2 className="text-2xl text-white text-center">{subtitle}<FlipWords words={words}/></h2>
          <div className="flex justify-center mt-8">
          <HoverBorderGradient>
            <button>
              <a href={buttonLink}>{buttonText}</a>
            </button>
          </HoverBorderGradient>
          </div>
      </div>
    </main>
    
  );
}

export default App

