
import '../components/homepage.css'
import { useNavigate } from 'react-router-dom'
import {Spotlight} from '../components/ui/spotlight-new'
import {FlipWords} from '../components/ui/flip-words'
import {HoverBorderGradient} from '../components/ui/hover-border-gradient'

export const HomePage: React.FC = () => {
    const navigate = useNavigate();
    const words = ["faster.", "easier.", "stress free.", "with AI."];
    const title = "ClassVoyant";
    const subtitle = "Pick your classes, get your schedule";
    const buttonText = "Find your classes";

    const handleButtonClick = () => {
        navigate('/semesters');

    };

    return (
        <main className="relative min-h-screen w-full bg-black/[0.96] antialiased bg-grid-white/[0.02] overflow-hidden flex items-center justify-center">
          <Spotlight></Spotlight>
            <div className="relative z-10">
              <h1 className="main-title">{title}</h1>
              <h2 className="sub-title">{subtitle}<FlipWords words={words}/></h2>
              <div className="flex justify-center mt-8">
              <HoverBorderGradient>
                <button onClick={handleButtonClick}>
                    {buttonText}
                </button>
              </HoverBorderGradient>
              </div>
          </div>
        </main>
    );
};

