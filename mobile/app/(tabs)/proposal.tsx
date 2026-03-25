import { View, TextInput, Button } from 'react-native';
import { intelliflow } from '@intelliflow/crm-mobile-sdk';
import { useState } from 'react';

export default function ProposalScreen() {
  const [dealId, setDealId] = useState('123e4567-e89b-12d3-a456-426614174000');
  const [style, setStyle] = useState('Modern');

  const generate = async () => {
    const result = await intelliflow.generateProposal(dealId, style);
    alert(`Proposal generated!\nURL: ${result.url}`);
  };

  return (
    <View className="flex-1 p-4">
      <Text className="text-2xl font-bold">AI Proposal Builder</Text>
      <TextInput placeholder="Deal ID" value={dealId} onChangeText={setDealId} className="border p-2 my-2" />
      <TextInput placeholder="Style (Professional/Modern)" value={style} onChangeText={setStyle} className="border p-2 my-2" />
      <Button title="Generate Proposal with AI" onPress={generate} />
    </View>
  );
}