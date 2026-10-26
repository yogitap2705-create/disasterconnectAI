import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Register from "./pages/Register";
import Login from "./pages/Login";
import CitizenDashboard from "./pages/CitizenDashboard";
import VolunteerDashboard from "./pages/VolunteerDashboard";
import AdminDashboard from "./pages/AdminDashboard";
import ReportDisaster from "./pages/ReportDisaster";
import AIChatbot from "./pages/AIChatbot";
import Contact from "./pages/Contact";
import NotFound from "./pages/NotFound";
import MapPage from "./pages/MapPage";
import MyReports from "./pages/MyReports";
import SheltersPage from "./pages/SheltersPage";
import EmergencyDirectory from "./pages/EmergencyDirectory";
import MissingPersons from "./pages/MissingPersons";
import SafetyProtocols from "./pages/SafetyProtocols";
import VolunteerInbox from "./pages/VolunteerInbox";
import FloatingAIAssistant from "./components/FloatingAIAssistant";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/citizen" element={<CitizenDashboard />} />
        <Route path="/volunteer" element={<VolunteerDashboard />} />
        <Route path="/volunteer/inbox" element={<VolunteerInbox />} />
        <Route path="/volunteer-inbox" element={<VolunteerInbox />} />
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/report" element={<ReportDisaster />} />
        <Route path="/chatbot" element={<AIChatbot />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/map" element={<MapPage />} />
        <Route path="/myreports" element={<MyReports />} />
        <Route path="/shelters" element={<SheltersPage />} />
        <Route path="/directory" element={<EmergencyDirectory />} />
        <Route path="/emergency-directory" element={<EmergencyDirectory />} />
        <Route path="/missing-persons" element={<MissingPersons />} />
        <Route path="/safety-protocols" element={<SafetyProtocols />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
      <FloatingAIAssistant />
    </BrowserRouter>
  );
}

export default App;