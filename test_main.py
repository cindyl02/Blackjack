import main


def test_user_has_blackjack(capfd, monkeypatch):
    cards = [10, 11, 11, 5, 1]
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [10, 11]. Your score: 21.\n" in out
    assert "Computer cards: [11, 5, 1]. Computer score: 17.\n" in out
    assert "Blackjack! You win.\n" in out
    assert "Your cards: [10, 11]. Your score: 21. Computer's first card: 11\n" in out


def test_computer_and_user_both_have_blackjack(capfd, monkeypatch):
    cards = [10, 10, 11, 11]
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [10, 11]. Your score: 21.\n" in out
    assert "Computer cards: [10, 11]. Computer score: 21.\n" in out
    assert "It's a draw.\n" in out
    assert "Your cards: [10, 11]. Your score: 21. Computer's first card: 10\n" in out


def test_computer_has_blackjack(capfd, monkeypatch):
    cards = [1, 11, 16, 10]
    monkeypatch.setattr("builtins.input", lambda _: "no")
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [1, 16]. Your score: 17.\n" in out
    assert "Computer cards: [11, 10]. Computer score: 21.\n" in out
    assert "Computer has a blackjack. You lose.\n" in out
    assert "Your cards: [1, 16]. Your score: 17. Computer's first card: 11\n" in out


def test_user_score_over_21(capfd, monkeypatch):
    cards = [16, 11, 16, 7]
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [16, 16]. Your score: 32.\n" in out
    assert "Computer cards: [11, 7]. Computer score: 18.\n" in out
    assert "You went over. You lose.\n" in out
    assert "Your cards: [16, 16]. Your score: 32. Computer's first card: 11\n" in out


def test_user_draws_three_cards_score_over_21(capfd, monkeypatch):
    cards = [16, 11, 1, 7, 8]
    monkeypatch.setattr("builtins.input", lambda _: "yes")
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [16, 1, 8]. Your score: 25.\n" in out
    assert "Computer cards: [11, 7]. Computer score: 18.\n" in out
    assert "You went over. You lose.\n" in out
    assert "Your cards: [16, 1]. Your score: 17. Computer's first card: 11\n" in out
    assert "Your cards: [16, 1, 8]. Your score: 25. Computer's first card: 11\n" in out


def test_computer_score_over_21(capfd, monkeypatch):
    cards = [16, 11, 1, 5, 8, 10]
    monkeypatch.setattr("builtins.input", lambda _: "no")
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [16, 1]. Your score: 17.\n" in out
    assert "Computer cards: [5, 8, 1, 10]. Computer score: 24.\n" in out
    assert "Computer went over. You win.\n" in out
    assert "Your cards: [16, 1]. Your score: 17. Computer's first card: 11\n" in out


def test_user_draws_three_cards_win(capfd, monkeypatch):
    cards = [16, 11, 1, 6, 3]
    inputs = ["yes", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [16, 1, 3]. Your score: 20.\n" in out
    assert "Computer cards: [11, 6]. Computer score: 17.\n" in out
    assert "You win.\n" in out
    assert "Your cards: [16, 1]. Your score: 17. Computer's first card: 11\n" in out
    assert "Your cards: [16, 1, 3]. Your score: 20. Computer's first card: 11\n" in out


def test_user_draws_three_cards_lose(capfd, monkeypatch):
    cards = [16, 11, 1, 5, 1, 3]
    inputs = ["yes", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [16, 1, 1]. Your score: 18.\n" in out
    assert "Computer cards: [11, 5, 3]. Computer score: 19.\n" in out
    assert "You lose.\n" in out
    assert "Your cards: [16, 1]. Your score: 17. Computer's first card: 11\n" in out
    assert "Your cards: [16, 1, 1]. Your score: 18. Computer's first card: 11\n" in out


def test_user_draws_ace_replace_with_1_win(capfd, monkeypatch):
    inputs = ["yes", "yes", "no"]
    cards = [11, 16, 1, 2, 12, 5]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [1, 12, 1, 5]. Your score: 19.\n" in out
    assert "Computer cards: [16, 2]. Computer score: 18.\n" in out
    assert "You win.\n" in out
    assert "Your cards: [11, 1]. Your score: 12. Computer's first card: 16\n" in out
    assert "Your cards: [1, 12, 1]. Your score: 14. Computer's first card: 16\n" in out
    assert "Your cards: [1, 12, 1, 5]. Your score: 19. Computer's first card: 16\n" in out


def test_user_draws_ace_not_replaced_draw(capfd, monkeypatch):
    inputs = ["yes", "yes", "no"]
    cards = [11, 16, 1, 2, 1, 5]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [11, 1, 1, 5]. Your score: 18.\n" in out
    assert "Computer cards: [16, 2]. Computer score: 18.\n" in out
    assert "It's a draw.\n" in out
    assert "Your cards: [11, 1]. Your score: 12. Computer's first card: 16\n" in out
    assert "Your cards: [11, 1, 1]. Your score: 13. Computer's first card: 16\n" in out
    assert "Your cards: [11, 1, 1, 5]. Your score: 18. Computer's first card: 16\n" in out


def test_computer_draws_ace_replace_with_1_draw(capfd, monkeypatch):
    cards = [16, 11, 2, 2, 15]
    monkeypatch.setattr("builtins.input", lambda _: "no")
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [16, 2]. Your score: 18.\n" in out
    assert "Computer cards: [2, 15, 1]. Computer score: 18.\n" in out
    assert "It's a draw.\n" in out
    assert "Your cards: [16, 2]. Your score: 18. Computer's first card: 11\n" in out


def test_computer_draws_ace_not_replaced_draw(capfd, monkeypatch):
    cards = [16, 11, 2, 1, 6]
    monkeypatch.setattr("builtins.input", lambda _: "no")
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [16, 2]. Your score: 18.\n" in out
    assert "Computer cards: [11, 1, 6]. Computer score: 18.\n" in out
    assert "It's a draw.\n" in out
    assert "Your cards: [16, 2]. Your score: 18. Computer's first card: 11\n" in out


def test_computer_and_user_scores_over_21(capfd, monkeypatch):
    cards = [16, 11, 10, 2, 10, 10]
    monkeypatch.setattr("builtins.input", lambda _: "no")
    monkeypatch.setattr("main.draw_card", lambda: cards.pop(0))
    main.play_game()
    out, err = capfd.readouterr()
    assert "Your cards: [16, 10]. Your score: 26.\n" in out
    assert "Computer cards: [2, 10, 1, 10]. Computer score: 23.\n" in out
    assert "You went over. You lose.\n" in out
    assert "Your cards: [16, 10]. Your score: 26. Computer's first card: 11\n" in out


def test_draw_card():
    card = main.draw_card()
    assert 2 <= card <= 11
