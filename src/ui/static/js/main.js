document.addEventListener('DOMContentLoaded', () => {
    const syntheticForm = document.getElementById('synthetic-data-form');
    const rawForm = document.getElementById('raw-dataset-form');
    const resultsOutput = document.getElementById('results-output');

    syntheticForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        resultsOutput.textContent = 'Generating...';

        const formData = new FormData(syntheticForm);
        const data = Object.fromEntries(formData.entries());
        data.num_subjects = parseInt(data.num_subjects, 10);

        try {
            const response = await fetch('/api/generate-synthetic-data', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            const result = await response.json();
            resultsOutput.textContent = response.ok
                ? `Success!\n\n${JSON.stringify(result, null, 2)}`
                : `Error:\n\n${JSON.stringify(result, null, 2)}`;
        } catch (error) {
            resultsOutput.textContent = `An unexpected error occurred: ${error.message}`;
        }
    });

    rawForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        resultsOutput.textContent = 'Generating package...';

        const formData = new FormData(rawForm);
        const data = Object.fromEntries(formData.entries());
        data.num_subjects = parseInt(data.num_subjects, 10);
        data.domains = data.domains.split(',').map(d => d.trim()).filter(d => d);

        try {
            const response = await fetch('/api/generate-raw-dataset-package', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            const result = await response.json();
            resultsOutput.textContent = response.ok
                ? `Success!\n\n${JSON.stringify(result, null, 2)}`
                : `Error:\n\n${JSON.stringify(result, null, 2)}`;
        } catch (error) {
            resultsOutput.textContent = `An unexpected error occurred: ${error.message}`;
        }
    });
});
