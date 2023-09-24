'use client';

import { useChat } from 'ai/react';
import React, { useEffect, useState } from "react";

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit, data } = useChat();


  const [message, setMessage] = useState("Loading");
  const [people, setPeople] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8080/api/text")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        // message = 'Loading'
        // once data is retrieved
        // message = data.message
        setMessage(data.message);
        setPeople(data.people);
      });
  }, []);


  return (
    <div className="flex flex-col w-full max-w-md py-24 mx-auto stretch">
      {message}
      {messages.length > 0
        ? messages.map(m => (
            <div key={m.id} className="whitespace-pre-wrap">
              {m.role === 'user' ? 'User: ' : 'AI: '}
              {m.content}
            </div>
          ))
        : null}

    </div>
  );
}
