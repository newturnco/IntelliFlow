import { View, Text, Button } from 'react-native';
import { intelliflow } from '@intelliflow/crm-mobile-sdk';
import { useState } from 'react';

export default function LeadsScreen() {
  const [leads, setLeads] = useState<any[]>([]);

  const createLead = async () => {
    const lead = await intelliflow.createLead({ name: "Mobile Test Lead", email: "mobile@acme.com" });
    setLeads([...leads, lead]);
  };

  return (
    <View className="flex-1 p-4">
      <Text className="text-2xl font-bold">Leads</Text>
      <Button title="Create New Lead (AI Scored)" onPress={createLead} />
      {leads.map(l => <Text key={l.id}>{l.name} - Score: {l.ai_score}</Text>)}
    </View>
  );
}