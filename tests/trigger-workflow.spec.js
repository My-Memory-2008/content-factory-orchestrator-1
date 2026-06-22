const { test, expect } = require('@playwright/test');
const fs = require('fs');
const path = require('path');

test('Trigger Target GitHub Workflow via API Configuration', async ({ request }) => {
  // Read and parse the local JSON file
  const configPath = path.join(__dirname, '../scheduler-config.json');
  const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));

  console.log(`Preparing API request for repo: ${config.repo_owner}/${config.repo_name}`);
  console.log(`Targeting workflow file: ${config.workflow_file}`);

  const response = await request.post(
    `https://github.com{config.repo_owner}/${config.repo_name}/actions/workflows/${config.workflow_file}/dispatches`,
    {
      headers: {
        'Accept': 'application/vnd.github+json',
        'Authorization': `Bearer ${process.env.GH_TOKEN}`, // This system token remains required for GitHub authorization
        'X-GitHub-Api-Version': '2022-11-28',
      },
      data: {
        ref: config.branch, 
      },
    }
  );

  if (response.status() === 204) {
    console.log(`Success! GitHub has started executing ${config.workflow_file}`);
  } else {
    const errorBody = await response.text();
    console.error(`Failed to trigger workflow. Status: ${response.status()}`);
    console.error(`Response details: ${errorBody}`);
  }

  expect(response.status()).toBe(204);
});
