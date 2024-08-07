function darkMode(){

  // 현재 모드를 가져옴
  let mode = $('html').attr("data-bs-theme");

  // 현재 모드와 반대되는 모드로 설정
  if( mode == 'dark' ){
    $('html').attr("data-bs-theme", "light");
    $('.mode-change-btn').html('다크모드');
  }else{
    $('html').attr("data-bs-theme", "dark");
    $('.mode-change-btn').html('라이트모드');
  }
}
