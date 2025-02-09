document.addEventListener("DOMContentLoaded", () => {
    let transactions = [
        { type: "Incoming Money", amount: 500, date: "2025-02-10" },
        { type: "Withdrawals", amount: 2_500_000, date: "2025-01-20" },
        { type: "Payments", amount: 150, date: "2025-02-05" },
        { type: "Incoming Money", amount: 700, date: "2025-01-15" },
        { type: "Withdrawals", amount: 100, date: "2025-02-01" },
        { type: "Bank Deposit", amount: 6_000_000, date: "2025-02-03" },
        { type: "Bill Payment", amount: 12_000, date: "2025-02-10" },
        { type: "Bank Transfer", amount: 200_000, date: "2025-02-15" }
    ];

    const transactionTable = document.getElementById("transactionTable");
    const searchType = document.getElementById("searchType");
    const filterMonth = document.getElementById("filterMonth");
    const filterAmountRange = document.getElementById("filterAmountRange");

    function renderTransactions(filteredTransactions) {
        transactionTable.innerHTML = "";
        filteredTransactions.forEach((tx) => {
            const row = `<tr>
                <td class="border p-2">${tx.type}</td>
                <td class="border p-2">$${tx.amount.toLocaleString()}</td>
                <td class="border p-2">${tx.date}</td>
                <td class="border p-2"><button class="bg-blue-500 text-white px-2 py-1 rounded">View</button></td>
            </tr>`;
            transactionTable.innerHTML += row;
        });
    }

    function applyFilters() {
        let filteredTransactions = [...transactions];

        // Search by transaction type
        const searchValue = searchType.value.toLowerCase();
        if (searchValue) {
            filteredTransactions = filteredTransactions.filter(tx =>
                tx.type.toLowerCase().includes(searchValue)
            );
        }

        // Filter by month
        const selectedMonth = filterMonth.value;
        if (selectedMonth) {
            filteredTransactions = filteredTransactions.filter(tx =>
                tx.date.startsWith(selectedMonth)
            );
        }

        // Filter by amount range
        const selectedRange = filterAmountRange.value;
        if (selectedRange) {
            const [min, max] = selectedRange.split("-").map(Number);
            filteredTransactions = filteredTransactions.filter(tx =>
                tx.amount >= min && tx.amount <= max
            );
        }

        renderTransactions(filteredTransactions);
    }

    // Event Listeners
    searchType.addEventListener("input", applyFilters);
    filterMonth.addEventListener("change", applyFilters);
    filterAmountRange.addEventListener("change", applyFilters);

    // Initial Render
    renderTransactions(transactions);
});
