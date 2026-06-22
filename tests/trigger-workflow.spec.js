const { test, expect } = require('@playwright/test');

test('Trigger Target GitHub Workflow via Dynamic API Configuration', async ({ request }) => {
  // Read details passed dynamically from the loop environment
  const OWNER = process.env.RUN_OWNER;
  const REPO = process.env.RUN_REPO;
  const WORKFLOW_FILE = process.env.RUN_WORKFLOW;
  const BRANCH = process.env.RUN_BRANCH;

  console.log(`Sending API request to: ${OWNER}/${REPO}`);
  console.log(`Executing workflow file: ${WORKFLOW_FILE} on branch: ${BRANCH}`);

  const response = await request.post(
    `https://github.com{OWNER}/${REPO}/actions/workflows/${WORKFLOW_FILE}/dispatches`,
    {
      headers: {
        'Accept': 'application/vnd.github+json',
        'Authorization': `Bearer ${process.env.GH_TOKEN}`,
        'X-GitHub-Api-Version': '2022-11-28',
      },
      data: {
        ref: BRANCH,
      },
    }
  );

  if (response.status() === 204) {
    console.log(`Success! Started execution for ${WORKFLOW_FILE}`);
  } else {
    const errorBody = await response.text();
    console.error(`Failed to trigger ${WORKFLOW_FILE}. Status: ${response.status()}`);
    console.error(`Response details: ${errorBody}`);
  }

  expect(response.status()).toBe(204);
});
