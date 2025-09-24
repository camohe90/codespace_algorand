// src/components/Home.tsx
import { useWallet } from '@txnlab/use-wallet-react'
import React, { useState } from 'react'
import ConnectWallet from './components/ConnectWallet'
import Transact from './components/Transact'

interface HomeProps {}

const Home: React.FC<HomeProps> = () => {
  const [openWalletModal, setOpenWalletModal] = useState<boolean>(false)
  const [openDemoModal, setOpenDemoModal] = useState<boolean>(false)
  const [claimed, setClaimed] = useState<boolean>(false)
  const { activeAddress } = useWallet()

  const toggleWalletModal = () => setOpenWalletModal(!openWalletModal)
  const toggleDemoModal = () => setOpenDemoModal(!openDemoModal)

  const handleClaim = () => setClaimed(true)

  return (
    <div className="hero min-h-screen bg-gradient-to-br from-teal-400 via-cyan-400 to-sky-400">
      <div className="hero-content w-full">
        <div className="mx-auto max-w-lg w-full rounded-2xl bg-white/90 backdrop-blur shadow-xl p-8 text-center">
          {/* Encabezado */}
          <h1 className="text-4xl font-extrabold tracking-tight text-teal-700">
            Bienvenidos a al mejor demo de 2025 <span className="text-teal-900">Masterpass</span> 🎟️
          </h1>

          {/* Descripción corta */}
          <p className="mt-3 text-teal-700/90">
            gracias a Juan
          </p>

          {/* Botones principales */}
          <div className="mt-8 grid gap-3">
            {/* Botón existente: Connect Wallet (no cambia la lógica) */}
            <button
              data-test-id="connect-wallet"
              className="btn btn-primary w-full"
              onClick={toggleWalletModal}
            >
              Connect Wallet
            </button>

            {/* Botón para pagos usando Transact (mostrado si hay wallet activa) */}
            {activeAddress && (
              <button
                data-test-id="transactions-demo"
                className="btn btn-outline w-full"
                onClick={toggleDemoModal}
              >
                Send Payment
              </button>
            )}

            {/* Botón Get Your MasterPass */}
            <button
              className={`btn w-full ${claimed ? 'btn-success btn-disabled' : 'btn-accent'}`}
              onClick={handleClaim}
              disabled={claimed}
            >
              {claimed ? 'Ticket Claimed' : 'Get Your MasterPass'}
            </button>
          </div>

          {/* Mensaje de éxito después de reclamar */}
          {claimed && (
            <div className="mt-5 alert alert-success shadow">
              <span>You've claimed your ticket!</span>
            </div>
          )}

          {/* Modales existentes (sin cambiar su lógica) */}
          <ConnectWallet openModal={openWalletModal} closeModal={toggleWalletModal} />
          <Transact openModal={openDemoModal} setModalState={setOpenDemoModal} />
        </div>
      </div>
    </div>
  )
}

export default Home