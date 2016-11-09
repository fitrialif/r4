var INTERVAL = 1000;

$(document).keydown((e) => {
  if (e.keyCode == 37) {
    $('#left').addClass('active');
    sendMoveCommand('left');
  } else if (e.keyCode == 38) {
    $('#up').addClass('active');
  } else if (e.keyCode == 39) {
    $('#right').addClass('active');
  } else if (e.keyCode == 40) {
    $('#down').addClass('active');
  }
});

$(document).keyup((e) => {
  if (e.keyCode == 37) {
    $('#left').removeClass('active');
  } else if (e.keyCode == 38) {
    $('#up').removeClass('active');
  } else if (e.keyCode == 39) {
    $('#right').removeClass('active');
  } else if (e.keyCode == 40) {
    $('#down').removeClass('active');
  }
});

function sendMoveCommand (direction) {
  setInterval(() => {
    $.ajax({
      url: "localhost:5000/move/" + direction,
      type: 'POST',
      error: () => {
        //
      },
      success: (res) => {
        //
      }
    });
  }, INTERVAL);
}
