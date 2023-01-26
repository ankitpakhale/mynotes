import React from "react";
import { Link } from "react-router-dom";

// This will convert the data into date and time only
const getTime = (date) => {
  return new Date(date).toLocaleString();
};

// This function will generate the title
const getTitle = (note) => {
  let title = note.body.split("\n")[0];
  if (title.length > 45) {
    return title.splice(0, 45);
  }
  return title;
};

const getContent = (note) => {
  let title = getTitle(note);
  let content = note.body.replaceAll("\n", " ");
  content = content.replaceAll(title, "");

  if (content.length > 45) {
    return content.slice(0, 45) + "...";
  } else {
    return content;
  }
};

const ListItem = ({ note }) => {
  return (
    <Link to={`/notes/${note.id}/`}>
      <div className="notes-list-item">
        <h3>{getTitle(note)}</h3>
        <p>
          <span>{getTime(note.created)}</span>
          {getContent(note)}
        </p>
        {/* <p>
          <span>{getTime(note.updated)}</span>
        </p> */}
      </div>
    </Link>
  );
};

export default ListItem;
