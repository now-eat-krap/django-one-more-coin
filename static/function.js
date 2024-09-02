const button = document.querySelector('.mode-change-btn')
const icon = document.querySelector('i')
const userTheme = localStorage.getItem('theme')
let status = false

// 처음 이용객의 테마를 읽음
document.addEventListener('DOMContentLoaded', () => {
    if (userTheme === 'dark') {
        clickDarkMode()
    } else if (userTheme === 'light') {
        clickLightMode()
    }
})

// 버튼클릭
button.addEventListener('click', () => {
    if (status === false) {
        clickDarkMode()
    } else if (status === true) {
        clickLightMode()
    }
})

// 다크/라이트 전환이벤트
function clickDarkMode() {
    localStorage.setItem("theme", "dark")
    icon.className = "bi bi-moon h4"
    document.documentElement.setAttribute('data-bs-theme', 'dark')
    status = true
}
function clickLightMode() {
    localStorage.setItem("theme", "light")
    icon.className = "bi bi-sun h4"
    document.documentElement.setAttribute('data-bs-theme', 'light')
    status = false
}
