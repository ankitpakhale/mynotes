import { HashRouter as Router, Route, Routes } from "react-router-dom";

import "./App.css";
import Headers from "./components/Headers";
import NotePage from "./pages/NotePage";
import NotesListPage from "./pages/NotesListPage";

function App() {
  return (
    <Router>
      <div className="container dark">
        <div className="app">
          <Headers />
          <Routes>
            <Route path="/" exact element={<NotesListPage />} />
            <Route path="/notes/:id" exact element={<NotePage />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
