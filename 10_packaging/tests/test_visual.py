from posner.experiment import draw_fixation, draw_text, draw_frames, draw_stimulus


def test_draw_fixation(create_config, mock_window, mock_circle):
    draw_fixation(mock_window, create_config)
    mock_circle.assert_called_once_with(
        mock_window,
        radius=create_config.fix_radius,
        size=(1 / mock_window.aspect, 1),
        fillColor="white",
    )


def test_draw_frames(create_config, mock_window, mock_rect):
    draw_frames(mock_window, create_config, highlight="left")
    kwargs = [k for _, k in mock_rect.call_args_list]
    x_coords = [k["pos"][0] for k in kwargs]
    colors = [k["lineColor"] for k in kwargs]
    assert x_coords == [-0.5, 0.5]
    assert colors == ["red", "white"]


def test_draw_text(mock_window, mock_text, create_config):
    for msg, first_word in zip(
        ["hello", "goodbye", "block 1"], ["Welcome", "Thank", "Press"]
    ):
        draw_text(mock_window, message=msg, config=create_config)
        _, kwargs = mock_text.call_args
        text = kwargs["text"].split(" ")
        assert text[0] == first_word


def test_draw_stimulus(create_config, mock_window, mock_circle):
    draw_stimulus(mock_window, create_config, side="left")
    _, kwargs = mock_circle.call_args
    assert kwargs["pos"][0] == create_config.pos.left[0]
    assert kwargs["size"] == (1 / mock_window.aspect, 1)
    assert kwargs["radius"] == create_config.stim_radius
