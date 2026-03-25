import { Tabs } from 'expo-router';
export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="leads" options={{ title: 'Leads' }} />
      <Tabs.Screen name="deals" options={{ title: 'Deals' }} />
      <Tabs.Screen name="proposal" options={{ title: 'AI Proposal' }} />
      <Tabs.Screen name="ask-ai" options={{ title: 'Ask AI' }} />
    </Tabs>
  );
}