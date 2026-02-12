'use client'
import Link from "next/link"
import { useRouter } from "next/navigation"
import { Button } from 'react-bootstrap'
const AdminPage = () => {
    const router = useRouter()

    return (
        <div>
            
            <h1>Admin Page</h1>
            <Button onClick={() => {router.push('/')}}>
                return home
            </Button>
        </div>
    )
}
export default AdminPage