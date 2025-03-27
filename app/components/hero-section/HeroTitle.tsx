import { Button, Text, Group } from '@mantine/core';
import { motion } from 'framer-motion';
import { useState, useEffect } from 'react';

const texts = [
  'Check Broken Links',
  'Analyze SEO',
  'Detect Old Content',
  'Improve Website Performance',
];

export function HeroTitle() {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setIndex((prev) => (prev + 1) % texts.length);
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <>
    <div style={{backgroundColor: '#1A1B1E', alignContent: 'center', display: 'flex', justifyContent: 'center', marginTop: '70px' }}>
    <div style={{backgroundColor:'#1A1B1E' , height:'400px'}}></div>
    <div style={{ padding: '40px 0',minHeight: '100vh',
      backgroundColor: '#1A1B1E', alignContent: 'center', display: 'flex', justifyContent: 'center', marginTop: '400px' }}>
      {/* Centered container for text and button only */}
      <div
        style={{
          marginLeft: '100px',   // Adjust these if needed
          marginRight: '250px',  // for your sidebar or layout
          textAlign: 'center',
        }}
      >
        <h1
          style={{
            fontSize: '3rem',
            fontWeight: 800,
            marginBottom: '10px',
            color: '#fff',
          }}
        >
          Your{' '}
          <Text component="span" inherit style={{ color: '#00FFFF' }}>
            one-stop solution
          </Text>{' '}
          to
        </h1>

        <motion.h2
          key={texts[index]}
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -10 }}
          transition={{ duration: 0.5 }}
          style={{
            fontSize: '2.3rem',
            fontWeight: 700,
            color: '#FFFFFF',
            marginBottom: '15px',
          }}
        >
          {texts[index]}
        </motion.h2>

        <Text
          style={{
            fontSize: '1.3rem',
            fontWeight: 500,
            lineHeight: '1.8',
            margin: '0 auto',
            padding: '1rem',
            color: '#ccc',
          }}
        >
          Supercharge your website's SEO – analyze, detect broken links, and optimize performance with our cutting-edge tools!
        </Text>

        <Group
          style={{
            marginTop: '30px',
            gap: '15px',
            justifyContent: 'center',
          }}
        >
          <Button
            size="lg"
            variant="filled"
            style={{
              backgroundColor: '#00FFFF',
              color: '#000',
              padding: '12px 24px',
              fontSize: '1rem',
              fontWeight: 600,
            }}
          >
            Get Started
          </Button>
        </Group>
      </div>
    </div>
    </div>
    </>
  );
}
