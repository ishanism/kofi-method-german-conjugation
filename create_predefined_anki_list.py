# dürfen, müssen
# Only modal and auxillary verbs need simple past
# All else do not!
# Model Verbs do not have imperative and auxillary verbs do
verbs = """
⊙Ich sein müde.;Ich bin müde.;sein Indikativ_Präsens ich Present
⊙Du sein spät.;Du bist spät.;sein Indikativ_Präsens du Present
⊙Er sein hier.;Er ist hier.;sein Indikativ_Präsens er/sie/es Present
⊙Wir sein glücklich.;Wir sind glücklich.;sein Indikativ_Präsens wir Present
⊙Ihr sein bereit.;Ihr seid bereit.;sein Indikativ_Präsens ihr Present
⊙Sie sein Ärzte.;Sie sind Ärzte.;sein Indikativ_Präsens sie Present
Nachdem das Spiel begonnen hatte, sein sie angekommen.;Nachdem das Spiel begonnen hatte, ist sie angekommen.;sein Indikativ_Perfekt er/sie/es Present_Perfect
←Ich sein gestern im Park.;Ich war gestern im Park.;sein Indikativ_Präteritum ich Simple_Past
←Du sein vor einer Stunde hier.;Du warst vor einer Stunde hier.;sein Indikativ_Präteritum du Simple_Past
←Er sein letzte Woche krank.;Er war letzte Woche krank.;sein Indikativ_Präteritum er/sie/es Simple_Past
←Wir sein in der Vergangenheit glücklich.;Wir waren in der Vergangenheit glücklich.;sein Indikativ_Präteritum wir Simple_Past
←Ihr sein gestern Abend bereit.;Ihr wart gestern Abend bereit.;sein Indikativ_Präteritum ihr Simple_Past
←Sie sein früher Ärzte.;Sie waren früher Ärzte.;sein Indikativ_Präteritum sie Simple_Past
Wenn ich du sein.;Wenn ich du wäre.;sein Konjunktiv_II ich Subjunctive_II
Wenn du ich sein.;Wenn du ich wärest.;sein Konjunktiv_II du Subjunctive_II
Wenn er hier sein.;Wenn er hier wäre.;sein Konjunktiv_II er/sie/es Subjunctive_II
Wenn wir glücklich sein.;Wenn wir glücklich wären.;sein Konjunktiv_II wir Subjunctive_II
Wenn ihr bereit sein.;Wenn ihr bereit wäret.;sein Konjunktiv_II ihr Subjunctive_II
Wenn Sie Ärzte sein.;Wenn sie Ärzte wären.;sein Konjunktiv_II sie Subjunctive_II
Sein glücklich!;Sei glücklich!;sein Imperativ du Imperative

⊙Ich haben einen Hund.;Ich habe einen Hund.;haben Indikativ_Präsens ich Present
⊙Du haben ein Buch.;Du hast ein Buch.;haben Indikativ_Präsens du Present
⊙Es haben ein Problem.;Es hat ein Problem.;haben Indikativ_Präsens er/sie/es Present
⊙Wir haben eine Idee.;Wir haben eine Idee.;haben Indikativ_Präsens wir Present
⊙Ihr haben Zeit.;Ihr habt Zeit.;haben Indikativ_Präsens ihr Present
⊙Sie haben Geld.;Sie haben Geld.;haben Indikativ_Präsens sie Present
Nachdem sie den Kurs abgeschlossen hatte, haben sie eine bessere Stelle ___;Nachdem sie den Kurs abgeschlossen hatte, hat sie eine bessere Stelle gehabt.;haben Indikativ_Perfekt er/sie/es Present_Perfect
←Ich haben gestern einen neuen Freund gefunden.;Ich hatte gestern einen neuen Freund gefunden.;haben Indikativ_Präteritum ich Simple_Past
←Du haben letztes Jahr ein Auto gekauft.;Du hattest letztes Jahr ein Auto gekauft.;haben Indikativ_Präteritum du Simple_Past
←Es haben vor zwei Tagen geregnet.;Es hatte vor zwei Tagen geregnet.;haben Indikativ_Präteritum er/sie/es Simple_Past
←Wir haben in der Kindheit viel gespielt.;Wir hatten in der Kindheit viel gespielt.;haben Indikativ_Präteritum wir Simple_Past
←Ihr haben gestern Zeit für mich.;Ihr hattet gestern Zeit für mich.;haben Indikativ_Präteritum ihr Simple_Past
←Sie haben im letzten Monat viel erreicht.;Sie hatten im letzten Monat viel erreicht.;haben Indikativ_Präteritum sie Simple_Past
Wenn ich mehr Zeit haben.;Wenn ich mehr Zeit hätte.;haben Konjunktiv_II ich Subjunctive_II
Wenn du ein Buch haben.;Wenn du ein Buch hättest.;haben Konjunktiv_II du Subjunctive_II
Wenn es ein Problem haben.;Wenn es ein Problem hätte.;haben Konjunktiv_II er/sie/es Subjunctive_II
Wenn wir eine Idee haben.;Wenn wir eine Idee hätten.;haben Konjunktiv_II wir Subjunctive_II
Wenn ihr Zeit haben.;Wenn ihr Zeit hättet.;haben Konjunktiv_II ihr Subjunctive_II
Wenn Sie Geld haben.;Wenn Sie Geld hätten.;haben Konjunktiv_II sie Subjunctive_II
Haben Geduld!;Hab Geduld!;haben Imperativ du Imperative

⊙Ich werden Lehrer.;Ich werde Lehrer.;werden Indikativ_Präsens ich Present
⊙Du werden schneller.;Du wirst schneller.;werden Indikativ_Präsens du Present
⊙Er werden müde.;Er wird müde.;werden Indikativ_Präsens er/sie/es Present
⊙Wir werden alt.;Wir werden alt.;werden Indikativ_Präsens wir Present
⊙Ihr werden besser.;Ihr werdet besser.;werden Indikativ_Präsens ihr Present
⊙Sie werden reich.;Sie werden reich.;werden Indikativ_Präsens sie Present
Nachdem sie studiert hatte, ist sie Arzt geworden.;Nachdem sie studiert hatte, sie Arzt geworden.;werden Indikativ_Perfekt er/sie/es Present_Perfect
←Ich werden gestern zum Manager befördert.;Ich wurde gestern zum Manager befördert.;werden Indikativ_Präteritum ich Simple_Past
←Du werden vor einer Woche schneller.;Du wurdest vor einer Woche schneller.;werden Indikativ_Präteritum du Simple_Past
←Er werden gestern Abend müde.;Er wurde gestern Abend müde.;werden Indikativ_Präteritum er/sie/es Simple_Past
←Wir werden vor zehn Jahren alt.;Wir wurden vor zehn Jahren alt.;werden Indikativ_Präteritum wir Simple_Past
←Ihr werden letztes Spiel besser.;Ihr wurdet letztes Spiel besser.;werden Indikativ_Präteritum ihr Simple_Past
←Sie werden früher in diesem Jahr reich.;Sie wurden früher in diesem Jahr reich.;werden Indikativ_Präteritum sie Simple_Past
Wenn ich ein Vogel werden.;Wenn ich ein Vogel würde.;werden Konjunktiv_II ich Subjunctive_II
Wenn du schneller werden.;Wenn du schneller würdest.;werden Konjunktiv_II du Subjunctive_II
Wenn er müde werden.;Wenn er müde würde.;werden Konjunktiv_II er/sie/es Subjunctive_II
Wenn wir alt werden.;Wenn wir alt würden.;werden Konjunktiv_II wir Subjunctive_II
Wenn ihr besser werden.;Wenn ihr besser würdet.;werden Konjunktiv_II ihr Subjunctive_II
Wenn sie reich werden.;Wenn sie reich würden.;werden Konjunktiv_II sie Subjunctive_II
Werde besser!;Werde besser!;werden Imperativ du Imperative

⊙Ich dürfen nach Hause gehen.;Ich darf nach Hause gehen.;dürfen Indikativ_Präsens ich Present
⊙Du dürfen im Park spielen.;Du darfst im Park spielen.;dürfen Indikativ_Präsens du Present
⊙Er dürfen einen Kuchen essen.;Er darf einen Kuchen essen.;dürfen Indikativ_Präsens er/sie/es Present
⊙Wir dürfen jetzt gehen.;Wir dürfen jetzt gehen.;dürfen Indikativ_Präsens wir Present
⊙Ihr dürfen das Auto benutzen.;Ihr dürft das Auto benutzen.;dürfen Indikativ_Präsens ihr Present
⊙Sie dürfen die Einrichtungen nutzen.;Sie dürfen die Einrichtungen nutzen.;dürfen Indikativ_Präsens sie Present
Nachdem sie die Erlaubnis erhalten hatte, hat sie ins Kino gehen dürfen.;Nachdem er/sie/es die Erlaubnis erhalten hatte, hat er/sie/es ins Kino gehen dürfen.;dürfen Indikativ_Perfekt er/sie/es Present_Perfect
←Ich dürfen gestern allein nach Hause gehen.;Ich durfte gestern allein nach Hause gehen.;dürfen Indikativ_Präteritum ich Simple_Past
←Du dürfen ohne Erlaubnis ausgehen.;Du durftest ohne Erlaubnis ausgehen.;dürfen Indikativ_Präteritum du Simple_Past
←Er dürfen das Spiel nicht sehen.;Er durfte das Spiel nicht sehen.;dürfen Indikativ_Präteritum er/sie/es Simple_Past
←Wir dürfen bei der Party bleiben.;Wir durften bei der Party bleiben.;dürfen Indikativ_Präteritum wir Simple_Past
←Ihr dürfen die Süßigkeiten essen.;Ihr durftet die Süßigkeiten essen.;dürfen Indikativ_Präteritum ihr Simple_Past
←Sie dürfen den Film sehen.;Sie durften den Film sehen.;dürfen Indikativ_Präteritum sie Simple_Past
Wenn ich das machen dürfen.;Wenn ich das machen dürfte.;dürfen Konjunktiv_II ich Subjunctive_II
Wenn du hier bleiben dürfen.;Wenn du hier bleiben dürftest.;dürfen Konjunktiv_II du Subjunctive_II
Wenn er die Prüfung nochmal schreiben dürfen.;Wenn er die Prüfung nochmal schreiben dürfte.;dürfen Konjunktiv_II er/sie/es Subjunctive_II
Wenn wir wählen dürfen.;Wenn wir wählen dürften.;dürfen Konjunktiv_II wir Subjunctive_II
Wenn ihr mehr Freiheit haben dürfen.;Wenn ihr mehr Freiheit haben dürftet.;dürfen Konjunktiv_II ihr Subjunctive_II
Wenn sie kommen dürfen.;Wenn sie kommen dürften.;dürfen Konjunktiv_II sie Subjunctive_II

⊙Ich müssen früh schlafen gehen.;Ich muss früh schlafen gehen.;müssen Indikativ_Präsens ich Present
⊙Du müssen deine Hausaufgaben machen.;Du musst deine Hausaufgaben machen.;müssen Indikativ_Präsens du Present
⊙Es müssen gesund essen.;Es muss gesund essen.;müssen Indikativ_Präsens er/sie/es Present
⊙Wir müssen jetzt gehen.;Wir müssen jetzt gehen.;müssen Indikativ_Präsens wir Present
⊙Ihr müssen mehr Sport treiben.;Ihr müsst mehr Sport treiben.;müssen Indikativ_Präsens ihr Present
⊙Sie müssen pünktlich sein.;Sie müssen pünktlich sein.;müssen Indikativ_Präsens sie Present
Nachdem sie die Aufgabe bekommen hatte, hat sie sie erledigen müssen.;Nachdem er/sie/es die Aufgabe bekommen hatte, hat er/sie/es sie erledigen müssen.;müssen Indikativ_Perfekt er/sie/es Present_Perfect
←Ich müssen früh schlafen gehen.;Ich musste früh schlafen gehen.;müssen Indikativ_Präteritum ich Simple_Past
←Du müssen deine Hausaufgaben machen.;Du musstest deine Hausaufgaben machen.;müssen Indikativ_Präteritum du Simple_Past
←Er müssen zum Arzt gehen.;Er musste zum Arzt gehen.;müssen Indikativ_Präteritum er/sie/es Simple_Past
←Wir müssen das Projekt fertigstellen.;Wir mussten das Projekt fertigstellen.;müssen Indikativ_Präteritum wir Simple_Past
←Ihr müssen pünktlich sein.;Ihr musstet pünktlich sein.;müssen Indikativ_Präteritum ihr Simple_Past
←Sie müssen die Regeln befolgen.;Sie mussten die Regeln befolgen.;müssen Indikativ_Präteritum sie Simple_Past
Wenn ich das Buch lesen müssen.;Wenn ich das Buch lesen müsste.;müssen Konjunktiv_II ich Subjunctive_II
Wenn du früher aufstehen müssen.;Wenn du früher aufstehen müsstest.;müssen Konjunktiv_II du Subjunctive_II
Wenn er uns helfen müssen.;Wenn er uns helfen müsste.;müssen Konjunktiv_II er/sie/es Subjunctive_II
Wenn wir die Prüfung nochmal machen müssen.;Wenn wir die Prüfung nochmal machen müssten.;müssen Konjunktiv_II wir Subjunctive_II
Wenn ihr schneller arbeiten müssen.;Wenn ihr schneller arbeiten müsstet.;müssen Konjunktiv_II ihr Subjunctive_II
Wenn sie die Wahrheit sagen müssen.;Wenn sie die Wahrheit sagen müssten.;müssen Konjunktiv_II sie Subjunctive_II

⊙Ich können schwimmen.;Ich kann schwimmen.;können Indikativ_Präsens ich Present
⊙Du können ein Auto fahren.;Du kannst ein Auto fahren.;können Indikativ_Präsens du Present
⊙Es können Deutsch sprechen.;Es kann Deutsch sprechen.;können Indikativ_Präsens er/sie/es Present
⊙Wir können das Problem lösen.;Wir können das Problem lösen.;können Indikativ_Präsens wir Present
⊙Ihr können uns helfen.;Ihr könnt uns helfen.;können Indikativ_Präsens ihr Present
⊙Sie können die Antwort wissen.;Sie können die Antwort wissen.;können Indikativ_Präsens sie Present
Nachdem er den Kurs besucht hatte, hat er Klavier spielen können.;Nachdem er/sie/es den Kurs besucht hatte, hat er/sie/es Klavier spielen können.;können Indikativ_Perfekt er/sie/es Present_Perfect
←Ich können schwimmen lernen.;Ich konnte schwimmen lernen.;können Indikativ_Präteritum ich Simple_Past
←Du können das Rätsel lösen.;Du konntest das Rätsel lösen.;können Indikativ_Präteritum du Simple_Past
←Er können den Berg besteigen.;Er konnte den Berg besteigen.;können Indikativ_Präteritum er/sie/es Simple_Past
←Wir können uns treffen.;Wir konnten uns treffen.;können Indikativ_Präteritum wir Simple_Past
←Ihr können das Spiel gewinnen.;Ihr konntet das Spiel gewinnen.;können Indikativ_Präteritum ihr Simple_Past
←Sie können eine Reise machen.;Sie konnten eine Reise machen.;können Indikativ_Präteritum sie Simple_Past
Wenn ich fliegen können.;Wenn ich fliegen könnte.;können Konjunktiv_II ich Subjunctive_II
Wenn du das verstehen können.;Wenn du das verstehen könntest.;können Konjunktiv_II du Subjunctive_II
Wenn er uns sehen können.;Wenn er uns sehen könnte.;können Konjunktiv_II er/sie/es Subjunctive_II
Wenn wir das kaufen können.;Wenn wir das kaufen könnten.;können Konjunktiv_II wir Subjunctive_II
Wenn ihr kommen können.;Wenn ihr kommen könntet.;können Konjunktiv_II ihr Subjunctive_II
Wenn sie es ändern können.;Wenn sie es ändern könnten.;können Konjunktiv_II sie Subjunctive_II

⊙Ich sollen die Hausaufgaben machen.;Ich soll die Hausaufgaben machen.;sollen Indikativ_Präsens ich Present
⊙Du sollen früher schlafen.;Du sollst früher schlafen.;sollen Indikativ_Präsens du Present
⊙Er sollen den Bericht lesen.;Er soll den Bericht lesen.;sollen Indikativ_Präsens er/sie/es Present
⊙Wir sollen gesünder essen.;Wir sollen gesünder essen.;sollen Indikativ_Präsens wir Present
⊙Ihr sollen mehr Sport treiben.;Ihr sollt mehr Sport treiben.;sollen Indikativ_Präsens ihr Present
⊙Sie sollen pünktlich sein.;Sie sollen pünktlich sein.;sollen Indikativ_Präsens sie Present
Er hat den Bericht schreiben sollen.;Er hat den Bericht schreiben sollen.;sollen Indikativ_Perfekt er/sie/es Present_Perfect
←Ich sollen früher ankommen.;Ich sollte früher ankommen.;sollen Indikativ_Präteritum ich Simple_Past
←Du sollen mir helfen.;Du solltest mir helfen.;sollen Indikativ_Präteritum du Simple_Past
←Er sollen das Buch lesen.;Er sollte das Buch lesen.;sollen Indikativ_Präteritum er/sie/es Simple_Past
←Wir sollen zusammenarbeiten.;Wir sollten zusammenarbeiten.;sollen Indikativ_Präteritum wir Simple_Past
←Ihr sollen warten.;Ihr solltet warten.;sollen Indikativ_Präteritum ihr Simple_Past
←Sie sollen die Anweisungen befolgen.;Sie sollten die Anweisungen befolgen.;sollen Indikativ_Präteritum sie Simple_Past
Wenn ich mehr lernen sollen.;Wenn ich mehr lernen sollte.;sollen Konjunktiv_II ich Subjunctive_II
Wenn du zuhause bleiben sollen.;Wenn du zuhause bleiben solltest.;sollen Konjunktiv_II du Subjunctive_II
Wenn er früher schlafen gehen sollen.;Wenn er früher schlafen gehen sollte.;sollen Konjunktiv_II er/sie/es Subjunctive_II
Wenn wir Hilfe suchen sollen.;Wenn wir Hilfe suchen sollten.;sollen Konjunktiv_II wir Subjunctive_II
Wenn ihr das Angebot annehmen sollen.;Wenn ihr das Angebot annehmen solltet.;sollen Konjunktiv_II ihr Subjunctive_II
Wenn sie entscheiden sollen.;Wenn sie entscheiden sollten.;sollen Konjunktiv_II sie Subjunctive_II

⊙Ich wollen ein Eis essen.;Ich will ein Eis essen.;wollen Indikativ_Präsens ich Present
⊙Du wollen ins Kino gehen.;Du willst ins Kino gehen.;wollen Indikativ_Präsens du Present
⊙Er wollen ein neues Auto kaufen.;Er will ein neues Auto kaufen.;wollen Indikativ_Präsens er/sie/es Present
⊙Wir wollen verreisen.;Wir wollen verreisen.;wollen Indikativ_Präsens wir Present
⊙Ihr wollen das Spiel gewinnen.;Ihr wollt das Spiel gewinnen.;wollen Indikativ_Präsens ihr Present
⊙Sie wollen die Welt sehen.;Sie wollen die Welt sehen.;wollen Indikativ_Präsens sie Present
Nachdem sie Geld gespart hatte, hat sie reisen wollen.;Nachdem sie Geld gespart hatte, hat sie reisen wollen.;wollen Indikativ_Perfekt er/sie/es Present_Perfect
←Ich wollen ein Eis essen.;Ich wollte ein Eis essen.;wollen Indikativ_Präteritum ich Simple_Past
←Du wollen ins Kino gehen.;Du wolltest ins Kino gehen.;wollen Indikativ_Präteritum du Simple_Past
←Er wollen ein Auto kaufen.;Er wollte ein Auto kaufen.;wollen Indikativ_Präteritum er/sie/es Simple_Past
←Wir wollen verreisen.;Wir wollten verreisen.;wollen Indikativ_Präteritum wir Simple_Past
←Ihr wollen das Spiel sehen.;Ihr wolltet das Spiel sehen.;wollen Indikativ_Präteritum ihr Simple_Past
←Sie wollen ein neues Haus bauen.;Sie wollten ein neues Haus bauen.;wollen Indikativ_Präteritum sie Simple_Past
Wenn ich die Welt bereisen wollen.;Wenn ich die Welt bereisen wollte.;wollen Konjunktiv_II ich Subjunctive_II
Wenn du das Problem lösen wollen.;Wenn du das Problem lösen wolltest.;wollen Konjunktiv_II du Subjunctive_II
Wenn er mitkommen wollen.;Wenn er mitkommen wollte.;wollen Konjunktiv_II er/sie/es Subjunctive_II
Wenn wir gewinnen wollen.;Wenn wir gewinnen wollten.;wollen Konjunktiv_II wir Subjunctive_II
Wenn ihr teilnehmen wollen.;Wenn ihr teilnehmen wolltet.;wollen Konjunktiv_II ihr Subjunctive_II
Wenn sie es versuchen wollen.;Wenn sie es versuchen wollten.;wollen Konjunktiv_II sie Subjunctive_II

⊙Ich mögen Schokolade.;Ich mag Schokolade.;mögen Indikativ_Präsens ich Present
⊙Du mögen Fußball spielen.;Du magst Fußball spielen.;mögen Indikativ_Präsens du Present
⊙Er mögen Bücher lesen.;Er mag Bücher lesen.;mögen Indikativ_Präsens er/sie/es Present
⊙Wir mögen ins Theater gehen.;Wir mögen ins Theater gehen.;mögen Indikativ_Präsens wir Present
⊙Ihr mögen das neue Restaurant.;Ihr mögt das neue Restaurant.;mögen Indikativ_Präsens ihr Present
⊙Sie mögen reisen.;Sie mögen reisen.;mögen Indikativ_Präsens sie Present
Er hat den Film sehr mögen.;Er hat den Film sehr gemocht;mögen Indikativ_Perfekt er/sie/es Present_Perfect
←Ich mögen Schokolade.;Ich mochte Schokolade.;mögen Indikativ_Präteritum ich Simple_Past
←Du mögen Fußball spielen.;Du mochtest Fußball spielen.;mögen Indikativ_Präteritum du Simple_Past
←Er mögen Bücher lesen.;Er mochte Bücher lesen.;mögen Indikativ_Präteritum er/sie/es Simple_Past
←Wir mögen ins Kino gehen.;Wir mochten ins Kino gehen.;mögen Indikativ_Präteritum wir Simple_Past
←Ihr mögen das Konzert.;Ihr mochtet das Konzert.;mögen Indikativ_Präteritum ihr Simple_Past
←Sie mögen reisen.;Sie mochten reisen.;mögen Indikativ_Präteritum sie Simple_Past
Wenn ich Kuchen essen mögen.;Wenn ich Kuchen essen möchte.;mögen Konjunktiv_II ich Subjunctive_II
Wenn du schwimmen gehen mögen.;Wenn du schwimmen gehen möchtest.;mögen Konjunktiv_II du Subjunctive_II
Wenn er uns besuchen mögen.;Wenn er uns besuchen möchte.;mögen Konjunktiv_II er/sie/es Subjunctive_II
Wenn wir eine Party haben mögen.;Wenn wir eine Party haben möchten.;mögen Konjunktiv_II wir Subjunctive_II
Wenn ihr das Spiel spielen mögen.;Wenn ihr das Spiel spielen möchtet.;mögen Konjunktiv_II ihr Subjunctive_II
Wenn sie mehr Freizeit haben mögen.;Wenn sie mehr Freizeit haben möchten.;mögen Konjunktiv_II sie Subjunctive_II
"""

file_path = "ankipredefinedlist.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(verbs)
