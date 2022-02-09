export async function getPing() {
    return await fetch('/api/ping');
}

export async function getResults() {
    return await fetch('/api/get_results/MMV_POSITIVE');
}

export async function startMs2query() {
    void (await fetch('/api/run_ms2query'));
}