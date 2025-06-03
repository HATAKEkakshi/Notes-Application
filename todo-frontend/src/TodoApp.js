import React, { useState } from "react";

const API_BASE = "http://localhost:8000"; // Change if your backend URL is different

export default function TodoApp() {
  const [todoId, setTodoId] = useState("");
  const [todo, setTodo] = useState(null);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [status, setStatus] = useState("");
  const [message, setMessage] = useState("");
  const [newTitle, setNewTitle] = useState("");
  const [newDescription, setNewDescription] = useState("");
  const [newStatus, setNewStatus] = useState("pending");

  // Fetch To-Do by ID
  const readTodo = async () => {
    if (!todoId.trim()) return alert("Please enter To-Do ID");
    try {
      const res = await fetch(`${API_BASE}/read_todo?id=${todoId}`);
      if (!res.ok) throw new Error("To-Do not found");
      const data = await res.json();
      setTodo(data);
      setTitle(data.title);
      setDescription(data.description);
      setStatus(data.status);
      setMessage("");
    } catch (e) {
      setTodo(null);
      setMessage(e.message);
    }
  };

  // Update To-Do Status
  const updateStatus = async () => {
    if (!todoId.trim()) return alert("Please load a To-Do first");
    try {
      const res = await fetch(`${API_BASE}/update_todo_status?id=${todoId}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ status }),
      });
      if (!res.ok) throw new Error("Failed to update status");
      setMessage("Status updated successfully");
    } catch (e) {
      setMessage(e.message);
    }
  };

  // Update To-Do Description
  const updateDescription = async () => {
    if (!todoId.trim()) return alert("Please load a To-Do first");
    try {
      const res = await fetch(`${API_BASE}/update_todo_description?id=${todoId}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description }),
      });
      if (!res.ok) throw new Error("Failed to update description");
      setMessage("Description updated successfully");
    } catch (e) {
      setMessage(e.message);
    }
  };

  // Delete To-Do
  const deleteTodo = async () => {
    if (!todoId.trim()) return alert("Please load a To-Do first");
    if (!window.confirm("Are you sure you want to delete this To-Do?")) return;
    try {
      const res = await fetch(`${API_BASE}/delete_todo?id=${todoId}`, {
        method: "DELETE",
      });
      if (!res.ok) throw new Error("Failed to delete");
      setMessage("To-Do deleted successfully");
      // Reset form
      setTodo(null);
      setTodoId("");
      setTitle("");
      setDescription("");
      setStatus("");
    } catch (e) {
      setMessage(e.message);
    }
  };

  // Create new To-Do
  const createTodo = async () => {
    if (!newTitle.trim()) return alert("Please enter title for new To-Do");
    try {
      const now = new Date().toISOString();
      const res = await fetch(`${API_BASE}/create_todo`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: newTitle,
          description: newDescription,
          created_at: now,
          updated_at: now,
          status: newStatus,
        }),
      });
      if (!res.ok) throw new Error("Failed to create To-Do");
      const data = await res.json();
      setMessage(`To-Do created with ID: ${data.id}`);
      // Reset create form
      setNewTitle("");
      setNewDescription("");
      setNewStatus("pending");
    } catch (e) {
      setMessage(e.message);
    }
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">FastAPI To-Do App (Bootstrap Frontend)</h2>

      {/* Read / Update / Delete Section */}
      <div className="mb-5">
        <h4>Read / Update / Delete To-Do</h4>
        <div className="input-group mb-3" style={{ maxWidth: "400px" }}>
          <input
            type="text"
            className="form-control"
            placeholder="Enter To-Do ID"
            value={todoId}
            onChange={(e) => setTodoId(e.target.value)}
          />
          <button className="btn btn-primary" onClick={readTodo}>
            Load To-Do
          </button>
        </div>

        {todo && (
          <div>
            <div className="mb-3">
              <label className="form-label">Title</label>
              <input type="text" className="form-control" value={title} readOnly />
            </div>

            <div className="mb-3">
              <label className="form-label">Description</label>
              <textarea
                className="form-control"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                rows={3}
              />
              <button className="btn btn-secondary mt-2" onClick={updateDescription}>
                Update Description
              </button>
            </div>

            <div className="mb-3">
              <label className="form-label">Status</label>
              <select
                className="form-select"
                value={status}
                onChange={(e) => setStatus(e.target.value)}
              >
                <option value="pending">Pending</option>
                <option value="in_progress">In Progress</option>
                <option value="completed">Completed</option>
              </select>
              <button className="btn btn-secondary mt-2" onClick={updateStatus}>
                Update Status
              </button>
            </div>

            <button className="btn btn-danger" onClick={deleteTodo}>
              Delete To-Do
            </button>
          </div>
        )}
      </div>

      {/* Create New To-Do Section */}
      <div>
        <h4>Create New To-Do</h4>
        <div className="mb-3" style={{ maxWidth: "400px" }}>
          <label className="form-label">Title</label>
          <input
            type="text"
            className="form-control"
            value={newTitle}
            onChange={(e) => setNewTitle(e.target.value)}
          />
        </div>

        <div className="mb-3" style={{ maxWidth: "400px" }}>
          <label className="form-label">Description</label>
          <textarea
            className="form-control"
            value={newDescription}
            onChange={(e) => setNewDescription(e.target.value)}
            rows={3}
          />
        </div>

        <div className="mb-3" style={{ maxWidth: "400px" }}>
          <label className="form-label">Status</label>
          <select
            className="form-select"
            value={newStatus}
            onChange={(e) => setNewStatus(e.target.value)}
          >
            <option value="pending">Pending</option>
            <option value="in_progress">In Progress</option>
            <option value="completed">Completed</option>
          </select>
        </div>

        <button className="btn btn-success" onClick={createTodo}>
          Create To-Do
        </button>
      </div>

      {/* Message Display */}
      {message && (
        <div className="alert alert-info mt-4" role="alert">
          {message}
        </div>
      )}
    </div>
  );
}
