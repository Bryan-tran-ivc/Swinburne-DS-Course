<!-- photolookup.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <title>Photo Album</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: system-ui, sans-serif;
            background: #fff;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2.5rem 1rem;
        }

        .wrapper {
            width: 100%;
            max-width: 420px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem;
        }

        h2 {
            font-size: 18px;
            font-weight: 500;
            color: black;
            text-align: center;
            width: 100%;
        }

        form {
            width: 100%;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 1.5rem;
        }

        fieldset { border: none; padding: 0; }

        dl { display: flex; flex-direction: column; gap: 0.85rem; }
        dt { display: flex; flex-direction: column; gap: 4px; }

        label {
            font-size: 13px;
            color: black;
        }

        input[type="text"],
        input[type="date"] {
            width: 100%;
            padding: 8px 10px;
            font-size: 13px;
            border: 1px solid #ddd;
            border-radius: 6px;
            background: #fff;
            color: black;
            outline: none;
            transition: border-color .15s;
        }

        input[type="text"]:focus,
        input[type="date"]:focus { border-color: #999; }

        input[type="submit"] {
            width: 100%;
            padding: 10px;
            font-size: 14px;
            font-weight: 500;
            background: black;
            color: #fff;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: opacity .15s;
            margin-top: 0.5rem;
        }
        input[type="submit"]:hover { opacity: 0.85; }

        .footer-link {
            font-size: 13px;
            text-align: center;
        }
        .footer-link a {
            color: black;
            text-decoration: none;
        }
        .footer-link a:hover { text-decoration: underline; }
    </style>
</head>
<body>

<div class="wrapper">
    <h2>Photo Lookup</h2>

    <form name="lookup" id="lookup">
        <fieldset>
            <dl>
                <dt>
                    <label for="phototitle">Photo title:</label>
                    <input type="text" name="phototitle" id="phototitle" />
                </dt>
                <dt>
                    <label for="keyword">Keyword:</label>
                    <input type="text" name="keyword" id="keyword" />
                </dt>
                <dt>
                    <label for="fromdate">From date:</label>
                    <input type="date" name="fromdate" id="fromdate" />
                </dt>
                <dt>
                    <label for="todate">To date:</label>
                    <input type="date" name="todate" id="todate" />
                </dt>
                <dt>
                    <input type="submit" value="Search" />
                </dt>
            </dl>
        </fieldset>
    </form>

    <p class="footer-link"><a href="photouploader.php">Photo Uploader</a></p>
</div>

</body>
</html>