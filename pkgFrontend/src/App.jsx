import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [courses, setCourses] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchCourses()
  }, [])

  const fetchCourses = async () => {
    try {
      setLoading(true)
      const response = await fetch('http://localhost:8000/api/courses/')
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      setCourses(data)
      setError(null)
    } catch (err) {
      console.error('Error fetching courses:', err)
      setError('Failed to load courses. Please check if your Django server is running.')
    } finally {
      setLoading(false)
    }
  }
}

export default App