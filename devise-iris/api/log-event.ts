import type { VercelRequest, VercelResponse } from '@vercel/node';
import { adminDb } from './_lib/firebaseAdmin';

export default async function handler(req: VercelRequest, res: VercelResponse) {
  // Handle CORS preflight
  if (req.method === 'OPTIONS') {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    return res.status(204).end();
  }

  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed. Use POST.' });
  }

  // Set CORS headers for the main request
  res.setHeader('Access-Control-Allow-Origin', '*');

  try {
    const payload = req.body;

    // Basic validation to ensure required fields exist
    if (!payload || !payload.org_id || !payload.tool_name) {
      return res.status(400).json({ error: 'Missing required fields: org_id and tool_name are required.' });
    }

    // Prepare the document to save to Firestore
    const eventData = {
      org_id: payload.org_id,
      tool_name: payload.tool_name,
      domain: payload.domain || 'unknown',
      process_name: payload.process_name || 'unknown',
      risk_level: payload.risk_level || 'low',
      timestamp: payload.timestamp || new Date().toISOString(),
      device_id: payload.device_id || 'unknown',
      user_email: payload.user_email || 'unknown',
      category: payload.category || 'Other',
      is_approved: payload.is_approved ?? false,
      // Add a server-side timestamp for when the record was actually received
      received_at: new Date().toISOString()
    };

    // Write securely to the 'detection_events' collection using Firebase Admin
    const collectionRef = adminDb.collection('detection_events');
    const docRef = await collectionRef.add(eventData);

    // Return success
    return res.status(200).json({ success: true, message: 'Event logged successfully', id: docRef.id });

  } catch (error) {
    console.error('Error logging event to Firestore:', error);
    return res.status(500).json({ error: 'Internal Server Error while logging event.' });
  }
}
