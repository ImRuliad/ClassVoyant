import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { HomePage } from './pages/HomePage'
import { SemestersPage } from './pages/SemestersPage'

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/semesters" element={<SemestersPage />} />
      </Routes>
    </Router>

  );
}

export default App

