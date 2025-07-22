# TODO: Build a Machine-Readable Inventory of CDASH-Based CRFs

1. **Create CDISC Library Account and Obtain API Key**
   - Register for a free CDISC Library account.
   - Visit the "API Keys" tab and generate an API key.

2. **Configure API Request Headers**
   - Base URL: `https://library.cdisc.org/api`.
   - Include `Authorization: Bearer <api_key>` and `Accept: application/vnd.cdisc+json` headers for all requests.

3. **Discover Available CDASH IG Versions**
   - Send `GET /api/mdr/cdashig` to list IG versions.
   - Collect each version's title and `href` from `_links["versions"]`.

4. **Retrieve Domain-Level CRFs for Each IG Version**
   - For every IG version `href`, request the domain list via `_links["domains"]`.
   - Fetch each domain's JSON using its `href`.

5. **Handle Domains with Multiple Scenarios**
   - Check each domain response for `_links["scenarios"]`.
   - When scenarios exist, request each scenario URL to obtain separate CRF data.

6. **Capture Fields and Controlled Terminology**
   - Inspect the `fields` array in each CRF for CDASH variable info and codelist references.
   - Cache codelist JSON by NCI code so repeated references reuse the same data.

7. **Support Pagination**
   - Follow `_links["next"]` when present on paged endpoints until no next link remains.

8. **Respect API Rate Limits**
   - Limit to roughly 60 requests per minute (e.g., `time.sleep(0.2)` between calls).
   - Implement retry/back-off logic via `requests` adapters.

9. **Increase Network Robustness**
   - Wrap API calls in a retry mechanism (five tries with exponential back-off).
   - Handle temporary network or service errors gracefully.

10. **Record Version Metadata**
    - Save both the IG version string and the `standardRelease` date when storing CRF data.

11. **Validate Each CRF Against CDISC Schema**
    - Retrieve `cdash-form.schema.json` from `/api/schemas`.
    - Validate downloaded CRF JSON and fail fast on unexpected fields.

12. **Transform to Your Canonical Format**
    - Convert CRF JSON to your preferred representation (ODM, FHIR Questionnaire, custom JSON, etc.).

13. **Confirm Unsupported Elements**
    - Note that some narrative content (e.g., Assumptions sections) remains outside the API and must be handled separately if needed.
