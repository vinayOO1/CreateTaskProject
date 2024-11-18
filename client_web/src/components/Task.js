import React, { useState } from "react";

const Task = () => {
    const [message, setMessage] = useState("");

    const createTask = async () => {
        try {
            const response = await fetch("http://localhost:8000/task/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({}), // Sending an empty object
            });

            if (!response.ok) {
                throw new Error("Failed to create task");
            }

            const data = await response.json();
            setMessage(data.message || "Task created successfully!");
        } catch (error) {
            console.error("Error:", error);
            setMessage("Failed to create task");
        }
    };

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <button onClick={createTask} style={{ padding: "5px 10px" }}>
                Create Task
            </button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default Task;
