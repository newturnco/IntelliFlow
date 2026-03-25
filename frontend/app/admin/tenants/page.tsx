'use client';
import { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Input } from '@/components/ui/input';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

export default function TenantManagement() {
  const [tenants, setTenants] = useState([]);
  const [newTenant, setNewTenant] = useState({ name: '', domain: '' });

  useEffect(() => {
    fetch('/api/admin/tenants').then(res => res.json()).then(setTenants);
  }, []);

  const createTenant = async () => {
    const res = await fetch('/api/admin/tenants', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newTenant)
    });
    const data = await res.json();
    setTenants([...tenants, data]);
  };

  const updateStorage = async (tenantId: string, provider: string) => {
    await fetch(`/api/admin/tenants/${tenantId}/storage`, {
      method: 'PATCH',
      body: JSON.stringify({ storage_provider: provider })
    });
    // Refresh list
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-8">Tenant Management (Super Admin)</h1>
      
      {/* Create New Tenant */}
      <div className="mb-8 p-6 border rounded-xl">
        <h2 className="text-xl mb-4">Create New Tenant</h2>
        <Input placeholder="Company Name" value={newTenant.name} onChange={e => setNewTenant({...newTenant, name: e.target.value})} />
        <Input placeholder="Domain" value={newTenant.domain} onChange={e => setNewTenant({...newTenant, domain: e.target.value})} className="mt-4" />
        <Button onClick={createTenant} className="mt-6">Create Tenant + Auto Seed</Button>
      </div>

      {/* Tenants Table */}
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>ID</TableHead>
            <TableHead>Name</TableHead>
            <TableHead>Domain</TableHead>
            <TableHead>Storage Provider</TableHead>
            <TableHead>Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {tenants.map((t: any) => (
            <TableRow key={t.id}>
              <TableCell>{t.id}</TableCell>
              <TableCell>{t.name}</TableCell>
              <TableCell>{t.domain}</TableCell>
              <TableCell>
                <Select defaultValue={t.storage_provider} onValueChange={val => updateStorage(t.id, val)}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="azure">Azure Blob</SelectItem>
                    <SelectItem value="wasabi">Wasabi</SelectItem>
                    <SelectItem value="s3">AWS S3</SelectItem>
                    <SelectItem value="r2">Cloudflare R2</SelectItem>
                  </SelectContent>
                </Select>
              </TableCell>
              <TableCell>
                <Button variant="destructive" size="sm">Suspend</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}