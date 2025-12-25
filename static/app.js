// Token ve kullanıcı bilgisi al
const token = localStorage.getItem('token');
const user = JSON.parse(localStorage.getItem('user'));

// Sayfa yüklendiğinde kontrol
if (!token || !user) {
    window.location.href = '/';
}

// Rol Türkçeleştirme
function getRoleTurkce(role) {
    const roles = {
        'admin': 'Yönetici',
        'member': 'Üye'
    };
    return roles[role] || role;
}

// Durum Türkçeleştirme
function getStatusTurkce(status) {
    const statuses = {
        'borrowed': 'Ödünç Alındı',
        'returned': 'İade Edildi',
        'overdue': 'Gecikmeli İade'
    };
    return statuses[status] || status;
}

// XSS Koruması: HTML Escape
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Kullanıcı bilgisini göster
document.getElementById('userInfo').textContent = `${user.username} (${getRoleTurkce(user.role)})`;

// Admin kontrolü
if (user.role === 'admin') {
    document.querySelectorAll('.admin-only').forEach(el => {
        el.style.display = 'block';
    });
}

// API çağrısı için yardımcı fonksiyon
async function apiCall(url, method = 'GET', body = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    };

    if (body) {
        options.body = JSON.stringify(body);
    }

    const response = await fetch(url, options);
    return await response.json();
}

// Sekme değiştirme
function showTab(tabName) {
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });

    document.getElementById(tabName).classList.add('active');
    event.target.classList.add('active');

    // Veri yükle
    if (tabName === 'books') loadBooks();
    if (tabName === 'borrowings') loadMyBorrowings();
    if (tabName === 'fines') loadMyFines();
}

// Kitapları yükle
async function loadBooks() {
    const data = await apiCall('/api/books');
    const booksList = document.getElementById('booksList');

    if (data.success) {
        booksList.innerHTML = data.books.map(book => `
            <div class="item-card">
                <h4>${escapeHtml(book.title)}</h4>
                <p><strong>Yazar:</strong> ${escapeHtml(book.author)}</p>
                <p><strong>ISBN:</strong> ${escapeHtml(book.isbn) || 'Yok'}</p>
                <p><strong>Mevcut:</strong> ${book.available_copies} / ${book.total_copies}</p>
                ${book.available_copies > 0 ?
                    `<button class="btn btn-small" onclick="borrowBook(${book.id})">Ödünç Al</button>` :
                    `<p style="color: red;">Stokta yok</p>`
                }
            </div>
        `).join('');
    }
}

// Kitap ödünç al
async function borrowBook(bookId) {
    const data = await apiCall('/api/borrowings', 'POST', { book_id: bookId });

    if (data.success) {
        alert('Kitap ödünç alındı!');
        loadBooks();
    } else {
        alert(data.message);
    }
}

// Ödünç kitaplarımı yükle
async function loadMyBorrowings() {
    const data = await apiCall('/api/borrowings/my');
    const borrowingsList = document.getElementById('borrowingsList');

    if (data.success) {
        if (data.borrowings.length === 0) {
            borrowingsList.innerHTML = '<p>Ödünç aldığınız kitap yok.</p>';
            return;
        }

        borrowingsList.innerHTML = data.borrowings.map(b => `
            <div class="item-card">
                <p><strong>Kitap ID:</strong> ${b.book_id}</p>
                <p><strong>Ödünç Tarihi:</strong> ${new Date(b.borrow_date).toLocaleDateString('tr-TR')}</p>
                <p><strong>İade Tarihi:</strong> ${new Date(b.due_date).toLocaleDateString('tr-TR')}</p>
                <p><strong>Durum:</strong> <span class="status-${b.status}">${getStatusTurkce(b.status)}</span></p>
                ${b.status === 'borrowed' ?
                    `<button class="btn btn-small" onclick="returnBook(${b.id})">İade Et</button>` :
                    b.return_date ? `<p>İade Edildi: ${new Date(b.return_date).toLocaleDateString('tr-TR')}</p>` : ''
                }
            </div>
        `).join('');
    }
}

// Kitap iade et
async function returnBook(borrowingId) {
    const data = await apiCall(`/api/borrowings/${borrowingId}/return`, 'POST');

    if (data.success) {
        alert('Kitap iade edildi!');
        loadMyBorrowings();
        loadMyFines();
    } else {
        alert(data.message);
    }
}

// Cezalarımı yükle
async function loadMyFines() {
    const data = await apiCall('/api/fines/my/unpaid');
    const finesList = document.getElementById('finesList');

    if (data.success) {
        if (data.fines.length === 0) {
            finesList.innerHTML = '<p>Ödenmemiş cezanız yok.</p>';
            return;
        }

        finesList.innerHTML = `
            <p><strong>Toplam Borç:</strong> ${data.total_amount} TL</p>
            ${data.fines.map(fine => `
                <div class="item-card">
                    <p><strong>Tutar:</strong> ${fine.amount} TL</p>
                    <p><strong>Durum:</strong> ${fine.paid ? 'Ödendi' : 'Ödenmedi'}</p>
                    ${!fine.paid ?
                        `<button class="btn btn-small" onclick="payFine(${fine.id})">Öde</button>` : ''
                    }
                </div>
            `).join('')}
        `;
    }
}

// Ceza öde
async function payFine(fineId) {
    const data = await apiCall(`/api/fines/${fineId}/pay`, 'POST');

    if (data.success) {
        alert('Ceza ödendi!');
        loadMyFines();
    } else {
        alert(data.message);
    }
}

// Kitap ara
async function searchBooks() {
    const query = document.getElementById('searchInput').value;
    if (!query) {
        loadBooks();
        return;
    }

    const data = await apiCall(`/api/books/search?q=${query}`);
    const booksList = document.getElementById('booksList');

    if (data.success) {
        booksList.innerHTML = data.books.map(book => `
            <div class="item-card">
                <h4>${escapeHtml(book.title)}</h4>
                <p><strong>Yazar:</strong> ${escapeHtml(book.author)}</p>
                <p><strong>Mevcut:</strong> ${book.available_copies} / ${book.total_copies}</p>
            </div>
        `).join('');
    }
}

// Yeni kitap ekle (Admin)
if (user.role === 'admin') {
    document.getElementById('addBookForm').addEventListener('submit', async (e) => {
        e.preventDefault();

        const bookData = {
            title: document.getElementById('bookTitle').value,
            author: document.getElementById('bookAuthor').value,
            isbn: document.getElementById('bookISBN').value,
            total_copies: parseInt(document.getElementById('bookCopies').value)
        };

        const data = await apiCall('/api/books', 'POST', bookData);

        if (data.success) {
            alert('Kitap eklendi!');
            document.getElementById('addBookForm').reset();
            loadBooks();
        } else {
            alert(data.message);
        }
    });
}

// Rapor al (Admin)
async function getReport() {
    const startDate = document.getElementById('reportStartDate').value;
    const endDate = document.getElementById('reportEndDate').value;

    if (!startDate || !endDate) {
        alert('Lütfen tarih aralığı seçin');
        return;
    }

    const data = await apiCall(`/api/borrowings/report?start_date=${startDate}&end_date=${endDate}`);
    const reportResult = document.getElementById('reportResult');

    if (data.success) {
        reportResult.innerHTML = `
            <h4>Rapor Sonuçları (${data.report.length} kayıt)</h4>
            ${data.report.map(r => `
                <div class="item-card">
                    <p><strong>Kullanıcı:</strong> ${escapeHtml(r.user_name)} (${escapeHtml(r.user_email)})</p>
                    <p><strong>Kitap:</strong> ${escapeHtml(r.book_title)} - ${escapeHtml(r.book_author)}</p>
                    <p><strong>Durum:</strong> ${getStatusTurkce(r.status)}</p>
                    <p><strong>Ceza:</strong> ${r.fine_amount} TL ${r.fine_paid ? '(Ödendi)' : '(Ödenmedi)'}</p>
                </div>
            `).join('')}
        `;
    } else {
        alert(data.message);
    }
}

// Çıkış
function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = '/';
}

// İlk yükleme
loadBooks();
