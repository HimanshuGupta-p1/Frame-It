import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import {useEffect, useState} from 'react'

function App() {
  const [todos, setTodos] = useState([]);
  useEffect(() =>  {
  axios.get('http://localhost:8005/api/v1/todos')
    .then((res) => {
      console.log(res);
      setTodos(res.data);
    })
  }, []);
  return (
    <div className="App">
      Todo App
      {
        todos.map((todo) => <div>
          <p>{todo.title}</p>
          <p>{todo.desc}</p>
          </div>)
      }
    </div>
  );
}

export default App;
