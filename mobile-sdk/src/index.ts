import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import * as SecureStore from 'expo-secure-store';

const API_BASE = 'https://api.your-domain.com';

class IntelliFlowSDK {
  private token: string | null = null;
  private tenantId: string | null = null;

  async login(email: string, password: string) {
    const res = await axios.post(`${API_BASE}/auth/login`, { email, password });
    this.token = res.data.access_token;
    this.tenantId = res.data.tenant_id;
    await SecureStore.setItemAsync('token', this.token!);
    await SecureStore.setItemAsync('tenantId', this.tenantId!);
    axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
  }

  async createLead(data: { name: string; email?: string; phone?: string }) {
    const res = await axios.post(`${API_BASE}/leads`, data);
    return res.data;
  }

  async getPipeline() {
    const res = await axios.get(`${API_BASE}/deals/pipeline`);
    return res.data;
  }

  async generateProposal(dealId: string, style: string = 'Professional', instructions = '') {
    const res = await axios.post(`${API_BASE}/ai/generate-proposal`, {
      deal_id: dealId,
      style,
      instructions,
    });
    return res.data; // { url, content }
  }

  // Ask AI (voice/text)
  async askAI(query: string) {
    const res = await axios.post(`${API_BASE}/ai/ask`, { query });
    return res.data;
  }

  // Canvas Studio sync (for custom UI on mobile)
  async saveCustomLayout(layoutJson: any) {
    const res = await axios.post(`${API_BASE}/canvas/save`, layoutJson);
    return res.data;
  }

  // Speech Assistant (uses device mic)
  async startVoiceCommand() {
    // Integrate expo-speech / expo-av here in your app
    console.log('Voice command started – connect to Web Speech API or device mic');
  }
}

export const intelliflow = new IntelliFlowSDK();
export default intelliflow;