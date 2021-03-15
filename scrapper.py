import twint

c = twint.Config()
c.Lang = "fr"
c.Search = "accouchement"
c.Store_csv = True
c.Output ="result"
c.Since = "2020-01-01"
c.Until = "2020-12-31"

twint.run.Search(c)