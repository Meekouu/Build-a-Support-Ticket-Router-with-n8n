# Build a Support Ticket Router with n8n

A local support-ticket automation project built with [n8n](https://n8n.io/), Docker Compose, and a small Python client. It accepts ticket data over a webhook, checks the ticket against routing rules, enriches it with mock on-call agent information, and returns a response that preserves the original ticket context.

Created by [Comi](https://nextwork.ai/portfolio/relieved_maroon_mysterious_tapir) · November 2026  
[Built on NextWork](https://nextwork.ai/projects/3cfb5c62-985e-4592-abc8-c0163f414a9f?utm_source=app&utm_medium=watermark&utm_campaign=referral)

## What it does

- Receives a JSON support ticket through an n8n webhook.
- Checks ticket messages for urgent keywords such as “crash” or “broken” and routes tickets using conditional logic.
- Demonstrates a premium-customer business rule using an OR condition. Because either condition can match, this rule intentionally admits a broader set of tickets than an AND condition.
- Calls the JSONPlaceholder REST API to simulate fetching on-call agent information.
- Preserves the original ticket fields alongside enrichment data in the workflow response.

The goal is to demonstrate how webhook intake, data enrichment, and conditional routing can reduce manual ticket sorting and direct urgent issues to an escalation queue.

## Project files

- `compose.yaml` — Runs n8n locally with persistent storage.
- `myscript.py` — Sends a sample JSON ticket to an n8n webhook and prints the HTTP response.

> The n8n workflow itself is configured in the n8n editor and is not included as an exported workflow file in this repository.

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) with Docker Compose
- Python 3
- The Python `requests` package

## Run n8n locally

From the project directory, start the n8n container:

```powershell
docker compose up -d
```

Open [http://localhost:5678](http://localhost:5678) and complete the initial n8n account setup. The Compose configuration binds n8n to `127.0.0.1` and stores its data in a named Docker volume, so it remains available across container restarts.

To stop n8n:

```powershell
docker compose down
```

The named volume is retained when the container is stopped, preserving n8n data.

## Configure and test the workflow

1. In the n8n editor, create a workflow with a Webhook node that accepts a JSON ticket payload.
2. Add conditional routing for urgent keywords and the premium-customer rule. Connect each branch to the appropriate response or queue-handling steps.
3. Add an HTTP Request node to retrieve mock agent data from JSONPlaceholder. Map the original webhook fields into the final response so enrichment does not replace the ticket.
4. Configure the Webhook node to respond when the last node finishes, returning the first entry as JSON.
5. Start listening for a test event in n8n, then set `WEBHOOK_URL` in `myscript.py` to the test webhook URL shown by the Webhook node. The sample URL in the script is specific to one n8n workflow and may need to be replaced.
6. Install the Python dependency and send the sample ticket:

   ```powershell
   python -m pip install requests
   python myscript.py
   ```

The sample ticket includes an urgent-sounding message and a `premium` customer tier. The script prints the HTTP status code and response body returned by n8n.

For production testing, activate or publish the workflow as appropriate for your n8n version, then update the client to use the production webhook URL instead of the test URL.

## Tools and concepts

- **n8n** — Visual, node-based workflow automation.
- **Docker Desktop and Docker Compose** — Local hosting with persistent n8n storage.
- **Webhooks** — HTTP entry points for incoming ticket events.
- **REST API enrichment** — Combining ticket data with information from an external API.
- **Conditional logic** — Sending tickets to different handling paths based on their content and customer attributes.

This project was completed in approximately an hour as a first hands-on exploration of automation workflows. It provides a starting point for building more advanced workflows with structured data handling, classification, and multiple services.
