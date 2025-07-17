import { useState } from 'react'

const Login = () => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [loginMsg, setLoginMsg] = useState(null)

    const onLogin = e => {
        e.preventDefault()
        const userCred = { username, password }
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userCred)
        }

        const checkUserCred = async () => {
            const res = await fetch('http://127.0.0.1:5000/login', options)
            const data = await res.json()
            if (data.response === 'ok') setLoginMsg(data.msg)
        }

        checkUserCred()
    }

    return (
        <div className='login-page'>
            {!loginMsg
                ? (
                    <form onSubmit={onLogin}>
                        <div>
                            <label htmlFor="username">Username</label>
                            <input
                                type="text"
                                onChange={e => setUsername(e.target.value)}
                            />
                        </div>

                        <div>
                            <label htmlFor="password">Password</label>
                            <input
                                type="password"
                                onChange={e => setPassword(e.target.value)}
                            />
                        </div>

                        <button type='submit'>Login</button>
                    </form>
                )
                : (
                    <div>
                        <h1>{loginMsg}</h1>
                    </div>
                )
            }
        </div>
    )
}

export default Login