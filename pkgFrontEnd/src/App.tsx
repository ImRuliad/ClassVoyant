import './App.css'
import {Spotlight} from './components/ui/spotlight-new'
import { FlipWords } from './components/ui/flip-words'
import { HoverBorderGradient } from './components/ui/hover-border-gradient'

function App() {
  const words = ["faster.", "easier.", "stress free.", "with AI."];

  return (
    <main className="relative min-h-screen w-full bg-black/[0.96] antialiased bg-grid-white/[0.02] overflow-hidden">
      <Spotlight />
      <section className="relative z-10 flex flex-col items-center justify-center min-h-[40rem] max-w-7xl mx-auto p-4 pt-20 md:pt-0 rounded-md">
        <header>
          <h1 className="text-4xl md:text-7xl font-bold text-center bg-clip-text text-transparent bg-gradient-to-b from-neutral-50 to-neutral-400 bg-opacity-50">
            Welcome to ClassVoyant <br />
          </h1>
        </header>
        <p className="mt-4 font-normal text-base text-neutral-300 max-w-lg text-center mx-auto">
          Less stress, better classes, fewer tabs. Find your course schedule <FlipWords words={words} />
        </p>
        <div className="mt-8 flex justify-center">
          <HoverBorderGradient
            containerClassName="rounded-full"
            as="a"
            // TODO: change to frontend url
            href="http://localhost:8000/api/courses/"
            className="dark:bg-black bg-white text-black dark:text-white flex items-center space-x-2"
            aria-label="Find your classes"
          >
            <span>Find your classes</span>
          </HoverBorderGradient>
        </div>
      </section>
    </main>
  );
}

export default App

