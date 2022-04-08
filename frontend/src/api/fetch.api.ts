export async function getPing() {
    return await fetch('/api/ping');
}

export async function getResultsMin() {
    return await fetch('/api/get_ms2query_results_min');
}

export async function getResultsFull() {
    return await fetch('/api/get_ms2query_results_full');
}

export async function getResultById(id: string) {
    return await fetch(`/api/find_ms2query_result/${id}`);
}

export async function startMs2query() {
    void (await fetch('/api/run_ms2query'));
}