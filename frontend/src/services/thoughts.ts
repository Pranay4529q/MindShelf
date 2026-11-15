import type { Thought } from "../types/thought";
const API = (import.meta.env.VITE_API_URL ?? "http://localhost:8000").replace(/\/$/, "");
let auth = "";
export function setCredentials(username: string, password: string) { auth = `Basic ${btoa(`${username}:${password}`)}`; }
export function clearCredentials() { auth = ""; }
async function request(path: string, options: RequestInit = {}) {
  const response = await fetch(`${API}${path}`, { ...options, headers: { "Authorization": auth, "Content-Type": "application/json", ...options.headers } });
  if (!response.ok) throw new Error(response.status === 401 ? "Invalid username or password" : `Request failed (${response.status})`);
  return response.status === 204 ? null : response.json();
}
export async function getThoughts(): Promise<Thought[]> { return request("/api/thoughts"); }
export async function addThought(content: string): Promise<Thought> { return request("/api/thoughts", {method:"POST",body:JSON.stringify({content})}); }
export async function removeThought(id: string): Promise<void> { await request(`/api/thoughts/${id}`, {method:"DELETE"}); }
export async function editThought(id: string, content: string): Promise<Thought> { return request(`/api/thoughts/${id}`, {method:"PUT",body:JSON.stringify({content})}); }
