import { useEffect, useState } from "react";
import axios from "axios";
import Note from "./components/Note";
import "./App.css";

function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/notes/")
      .then((res) => setNotes(res.data));
  }, []);

  console.log(notes);

  return (
    <div className="App">
        <img src="/logo-getit.png" />

      {notes.map((note) => (
        <Note key={`note__${note.id}`} title={note.title}>
          {note.content}
        </Note>
      ))}
    </div>
  );
}

export default App;