import React, { useState, useEffect } from 'react'

interface Semester {
    semester_name: string,
}

export const SemestersPage: React.FC = () => {
    const semester_url = 'http://localhost:8000/api/semesters/'
    const [semesters, setSemesters] = useState<Semester[]>([]);
    const [error, setError] = useState<string | null>(null);
    
    useEffect(() => {
        fetchSemesters();
    }, [])

    const fetchSemesters = async () => {
        try{
           const response = await fetch(semester_url);
           if (!response.ok){
            throw new Error('Failed to fetch semesters');
           } 
            const data = await response.json();
            setSemesters(data.results || data);
        } catch (err) {
            setError(err instanceof Error ? err.message : 'An error occured');
        }
    }

    if(error) {
        return (
            <div className="flex items-center justify-center">
                <div className="text-red-400 text-xl">Error: {error}</div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-black/[0.96] flex items-center justify-center">
            <header>
                <h1 className="text-white text-4xl">Hello from Semesters Page!</h1>
            </header>
        </div>
    )
}
