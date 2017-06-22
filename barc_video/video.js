
function video() {
	$.get("/video",function (_data) {
		// Object.values(_data)
		for (var i = 1; i <=4 ; i++) {
			video = document.getElementById('video'+i)
			var source = document.createElement('source');
			source.setAttribute('src', Object.values(_data)[i]);
			source.setAttribute('id',"video")
			video.appendChild(source);
			$('#video'+i).click(function(){this.paused?this.play():this.pause();});
		}
		
	})
}

video()